(function(){

    var FIELDS = {
        phone_number: 'Número de teléfono',
        city: 'Ciudad',
        name: 'Nombre',
        content: 'Comentarios',
        address: 'Dirección',
        email: 'E-mail'
    };

    var module = angular.module('Repuestazo', ['ui.bootstrap', 'ngCookies']);
    module.provider('Settings', ['$windowProvider', function($wp) {
        /**
         * Este provider (SettingsProvider) tiene un provider que
         * en su $get devuelve un objeto que, considerando $window, crea un prefetch
         * de variables similar al que uno haria en un modulo de settings en el servidor,
         * pero esto ocurriria tomando variables desde el espacio global.
         */
        var $window = $wp.$get();
        /*
         diccionario de valores obtenidos como settings.
         */
        this._fetched = {};
        /*
         la instancia provista no es mas que el diccionario coleccionado.
         */
        this.$get = function() {
            return this._fetched;
        };
        /*
         collect toma un conjunto de variables {nombre: default}.
         esto chupa todas las variables con dichos nombres desde el
         $window y, si no las encuentra, les popula un valor predeterminado.
         lo obtenido o preopopulado permanece en _fetched.
         */
        this.collect = function(expected_settings) {
            var fetched = this._fetched;
            if (angular.equals(fetched, {})) {
                angular.forEach(expected_settings, function(value, key) {
                    fetched[key] = $window[key] || value;
                });
            }
        };
    }]);
    module.controller('ComingSoon', ['$rootScope', '$scope', '$modal',
                                     function($rootScope, $scope, $modal){
        $scope.contactForm = function(){
            $scope.modalState = 'closed';
            if ($rootScope.modalState != 'opened') {
                $rootScope.modalState = 'opened';
                var instance = $modal.open({
                    keyboard: true,
                    backdrop: true,
                    templateUrl: 'contact.us.html',
                    windowClass: 'form-dialog',
                    scope: $scope,
                    controller: ['$scope', '$http', '$modalInstance', 'Settings', '$cookies',
                                 function($scope, $http, $modalInstance, settings, $cookies){
                        $scope.success = false;
                        $scope.form = {
                            name: '',
                            email: '',
                            address: '',
                            phone_number: '',
                            city: '',
                            content: ''
                        };
                        $scope.send = function() {
                            $scope.errors = null;
                            $http
                                .post(settings.CONTACT_URL, $scope.form, {
                                    headers: {
                                        'Accept-Language': 'es-ec',
                                        'X-CSRFToken': $cookies['csrftoken']
                                    }
                                })
                                .success(function(data, status, headers, config){
                                    $scope.success = true;
                                })
                                .error(function(data, status, headers, config){
                                    if (status == 400) {
                                        var errors = [];
                                        angular.forEach(data, function(items, field){
                                            if (field != '__all__') {
                                                angular.forEach(items, function(value, index){
                                                    items[index] = (FIELDS[field] || field) + ': ' + value;
                                                });
                                            }
                                            Array.prototype.push.apply(errors, items);
                                        });
                                        $scope.errors = errors;
                                    } else if (status == 429) {
                                        $scope.errors = ['Debes esperar un tiempo entre diferentes consultas'];
                                    } else {
                                        $scope.errors = ['Ocurrió un error interno. Consule al administrador del sitio si el mismo persiste'];
                                    }
                                })
                        }
                    }]
                });
                instance.result.then(function(){
                    $rootScope.modalState = 'closed';
                });
            }
        };
    }]);
    module.config(['SettingsProvider', function(settings){
        settings.collect({'STATIC_URL': '/static/', 'CONTACT_URL': ''})
    }]);

})();
