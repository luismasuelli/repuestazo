(function(){

    var Index = angular.module('Index', ['ui.router', 'ngCookies']);

    Index.controller('Index.Main', ['$rootScope', '$state', '$http', '$interval', '$timeout', function($rootScope, $state, $http, $interval, $timeout) {
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
            //TODO poner los datos buenos
            name: 'Bomba de Gasolina Corsa',
            offer: '60% DSCT.',
            foot: 'Promoción por Tiempo Limitado'
        };
        $rootScope.randomImage = {
            "name": "Dummy Random Banner",
            "description": "Dummy Random Source",
            "random": {
                "code": 1,
                "name":"Dummy Banner",
                "description": "Dummy Banner Result",
                "width":797,
                "height":738,
                "image":"http://127.0.0.1:8000/media/banner/BigBanner.png"
            }
        };
        $http
            .get('/ads/random-banner/bigfront', {})
            .success(function(data){
                $rootScope.randomImage = data;
            })
            .error(function(){

            });
        $rootScope.promos = [{"id":0,"product":"Cargando las ofertas","brand":"","model":"","year":null,"discount":""}];
        $http
            .get('/replacements/cheap', {})
            .success(function(data){
                $rootScope.promos = data;
                $interval(function(){
                    $rootScope.fading = true; //marcamos fading en primer elemento (se activara una clase)
                    $timeout(function(){
                        //se completa el fade (esperamos el mismo tiempo que dura la transicion) y movemos el elemento
                        //bien hacia el final
                        $rootScope.promos.push($rootScope.promos.shift());
                    }, 1500);
                }, 1500);
            })
            .error(function(){
                $rootScope.promos = [{"id":0,"product":"Hubo un error al cargar las ofertas","brand":"","model":"","year":null,"discount":""}];
            });
        $rootScope.displayPromo = function(promo) {
            var content = promo.product;
            if (promo.brand) {
                content = content + ' ' + promo.brand;
            }
            if (promo.model) {
                content = content + ' ' + promo.model;
            }
            if (parseFloat(promo.discount)) {
                content = content + ' con un descuento de ' + promo.discount;
            }
            return content;
        };
        $rootScope.popupPromo = function(id) {
            if (id) {
                //TODO implementar
                var url = '/replacements/cheap/' + id;
                console.log('Accediendo a ' + url);
            }
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
