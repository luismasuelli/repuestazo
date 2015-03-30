(function(){

    var Index = angular.module('Index', ['ui.router', 'ngCookies']);

    Index.controller('Index.Main', ['$state', function($state){
        $state.go('home');
    }]);

    Index.controller('Index.Home', ['$state', function($state){

    }]);
    Index.controller('Index.Promociones', ['$state', function($state){

    }]);
    Index.controller('Index.Informate', ['$state', function($state){

    }]);
    Index.controller('Index.Garantia', ['$state', function($state){

    }]);
    Index.controller('Index.PromoIzquierda', ['$state', function($state){

    }]);
    Index.controller('Index.PromoDerecha', ['$state', function($state){

    }]);
    Index.controller('Index.Formulario', ['$rootScope', '$scope', '$http', '$state', '$stateParams', '$cookies',
                                          function($rootScope, $scope, $http, $state, $stateParams, $cookies){
        var headers = {
            'Accept-Language': 'es-ec',
            'X-CSRFToken': $cookies['csrftoken']
        };
        var tracking = $stateParams.tracking;
    }]);

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

    Index.config(['$stateProvider', 'SettingsProvider', function($stateProvider, settingsProvider){
        settingsProvider.collect({
            'STATIC_URL': '/static/',
            'MEDIA_URL': '/media/'
        });

        var settings = settingsProvider.$get();

        $stateProvider
            .state('home', {
                templateUrl: settings.STATIC_URL + 'partials/home.html',
                controller: 'Index.Home'
            })
            .state('promociones', {
                templateUrl: settings.STATIC_URL + 'partials/promociones.html',
                controller: 'Index.Promociones'
            })
            .state('informate', {
                templateUrl: settings.STATIC_URL + 'partials/informate.html',
                controller: 'Index.Informate'
            })
            .state('garantia', {
                templateUrl: settings.STATIC_URL + 'partials/garantia.html',
                controller: 'Index.Garantia'
            })
            .state('promo-izquierda', {
                templateUrl: settings.STATIC_URL + 'partials/promo-izquierda.html',
                controller: 'Index.PromoIzquierda'
            })
            .state('promo-derecha', {
                templateUrl: settings.STATIC_URL + 'partials/promo-derecha.html',
                controller: 'Index.PromoDerecha'
            })
            .state('formulario', {
                params: ['tracking'],
                templateUrl: settings.STATIC_URL + 'partials/formulario.html',
                controller: 'Index.Formulario'
            });
    }]);

})();
