(function(){

    var Index = angular.module('Index', ['ui.router', 'ngCookies']);

    Index.controller('Index.Main', ['$rootScope', '$state', function($rootScope, $state){
        $rootScope.go = {
            home: function() { $state.go('home') },
            promociones: function() { $state.go('promociones') },
            informate: function() { $state.go('informate') },
            garantia: function() { $state.go('garantia') },
            promoIzquierda: function() { $state.go('promo-izquierda') },
            promoDerecha: function() { $state.go('promo-derecha') },
            formulario: function(tag) { $state.go('promo-derecha', {tracking: tag}) }
        };
        $rootScope.randomText = {
            name: 'Bomba de Gasolina Corsa',
            offer: '60% DSCT.',
            foot: 'Promoción por Tiempo Limitado'
        };
        $state.go('home');
    }]);

    Index.controller('Index.Home', ['$scope', function($scope){

    }]);
    Index.controller('Index.Promociones', ['$scope', function($scope){

    }]);
    Index.controller('Index.Informate', ['$scope', function($scope){

    }]);
    Index.controller('Index.Garantia', ['$scope', function($scope){

    }]);
    Index.controller('Index.PromoIzquierda', ['$scope', function($scope){

    }]);
    Index.controller('Index.PromoDerecha', ['$scope', function($scope){

    }]);
    Index.controller('Index.Formulario', ['$rootScope', '$scope', '$http', '$state', '$stateParams', '$cookies',
                                          function($rootScope, $scope, $http, $state, $stateParams, $cookies){
        var headers = {
            'Accept-Language': 'es-ec',
            'X-CSRFToken': $cookies['csrftoken']
        };
        var tracking = $stateParams.tracking;
    }]);

    Index.provider('Settings', ['$windowProvider', function($wp) {
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
                templateUrl: settings.STATIC_URL + 'pages/partials/home.html',
                controller: 'Index.Home'
            })
            .state('promociones', {
                templateUrl: settings.STATIC_URL + 'pages/partials/promociones.html',
                controller: 'Index.Promociones'
            })
            .state('informate', {
                templateUrl: settings.STATIC_URL + 'pages/partials/informate.html',
                controller: 'Index.Informate'
            })
            .state('garantia', {
                templateUrl: settings.STATIC_URL + 'pages/partials/garantia.html',
                controller: 'Index.Garantia'
            })
            .state('promo-izquierda', {
                templateUrl: settings.STATIC_URL + 'pages/partials/promo-izquierda.html',
                controller: 'Index.PromoIzquierda'
            })
            .state('promo-derecha', {
                templateUrl: settings.STATIC_URL + 'pages/partials/promo-derecha.html',
                controller: 'Index.PromoDerecha'
            })
            .state('formulario', {
                params: ['tracking'],
                templateUrl: settings.STATIC_URL + 'pages/partials/formulario.html',
                controller: 'Index.Formulario'
            });
    }]);

})();
