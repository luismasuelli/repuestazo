(function(){

    var Index = angular.module('Index', ['ui.router', 'ngCookies']);

    Index.controller('Index.Main', ['$rootScope', '$state', '$http', '$interval', '$timeout', 'Settings', function($rootScope, $state, $http, $interval, $timeout, settings) {
        $rootScope.STATIC_URL = settings.STATIC_URL;
        $rootScope.go = {
            home: function() { $state.go('home') },
            promociones: function() { $state.go('promociones') },
            informate: function() { $state.go('informate') },
            garantia: function() { $state.go('garantia') },
            formulario: function(tag) { $state.go('formulario', {tracking: tag}) },
            blog: function(){ $state.go('blog') }
        };
        $rootScope.playHomeReel= function() {
            $rootScope.homeReelPlaying = true;
        };
        $rootScope.stopHomeReel = function() {
            $rootScope.homeReelPlaying = false;
        };
        $rootScope.homeReelPlaying = false;
        $rootScope.randomText = {
            //TODO poner los datos buenos
            name: 'Bomba de Gasolina Corsa',
            offer: '60% DSCT.',
            foot: 'Promoción por Tiempo Limitado'
        };
        $http
            .get('/ads/random-text-set/rtextfront', {})
            .success(function(data){
                var entries = data.random.entries;
                $rootScope.randomText = {};
                if (entries) {
                    angular.forEach(entries, function(value){
                        $rootScope.randomText[value.text_field.code] = value.value;
                    });
                }
            })
            .error(function(){

            });
        $rootScope.reel = {
            "image_list": [
                {
                    "name": "Dummy Reel Image 1",
                    "description": "Dummy Reel Image 1 Description",
                    "image": "http://127.0.0.1:8000/media/reel/dummy1.png"
                }, {
                    "name": "Dummy Reel Image 2",
                    "description": "Dummy Reel Image 2 Description",
                    "image": "http://127.0.0.1:8000/media/reel/dummy2.png"
                }, {
                    "name": "Dummy Reel Image 3",
                    "description": "Dummy Reel Image 3 Description",
                    "image": "http://127.0.0.1:8000/media/reel/dummy3.png"
                }, {
                    "name": "Dummy Reel Image 4",
                    "description": "Dummy Reel Image 4 Description",
                    "image":" http://127.0.0.1:8000/media/reel/dummy4.png"
                }
            ],
            "code":"reelfront",
            "name":"Reel del Home",
            "description":"Reel de la pagina principal",
            "link_default":"",
            "link_prevails":true
        };
        $http
            .get('/ads/reel/reelfront', {})
            .success(function(data){
                $rootScope.reel = data;
                $rootScope.reel.current = null;
                var index = 0;
                $interval(function(){
                    index++;
                    if (index == $rootScope.reel.image_list.length) {
                        index = 0;
                    }
                    $rootScope.reel.current = $rootScope.reel.image_list[index];
                }, 4000);
            })
            .error(function(){

            });
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
        $rootScope.bannerIzquierda = {};
        $http
            .get('/ads/banner/leftfoot', {})
            .success(function(data){
                $rootScope.bannerIzquierda = data;
            })
            .error(function(){

            });
        $rootScope.bannerCentro = {};
        $http
            .get('/ads/banner/midfoot', {})
            .success(function(data){
                $rootScope.bannerCentro = data;
            })
            .error(function(){

            });
        $rootScope.bannerDerecha = {};
        $http
            .get('/ads/banner/rightfoot', {})
            .success(function(data){
                $rootScope.bannerDerecha = data;
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
                        if ($rootScope.homeReelPlaying) {
                            $rootScope.promos.push($rootScope.promos.shift());
                        }
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
                content = content + ' descuento ' + promo.discount;
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
        $rootScope.textoGarantia = "Cargando ...";
        $http
            .get('/ads/text-set/garantia', {})
            .success(function(data){
                $rootScope.textoGarantia = data.entries[0].value;
            });
        $state.go('home');
        $rootScope.todasLasPromociones = [];
        $http
            .get('ads/reel/reelpromos', {})
            .success(function(data) {
                $rootScope.todasLasPromociones = data.image_list;
            });
        $rootScope.imagenInformate = {};
        $http
            .get('ads/banner/informate', {})
            .success(function(data) {
                $rootScope.imagenInformate = data;
            })
    }]);

    Index.controller('Index.Home', ['$scope', function($scope){

    }]);
    Index.controller('Index.Promociones', ['$scope', function($scope){

    }]);
    Index.controller('Index.Informate', ['$scope', function($scope){

    }]);
    Index.controller('Index.Garantia', ['$scope', function($scope){

    }]);
    Index.controller('Index.Blog', ['$scope', function($scope){

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
            .state('blog', {
                templateUrl: settings.STATIC_URL + 'pages/partials/blog.html',
                controller: 'Index.Blog'
            })
            .state('formulario', {
                params: ['tracking'],
                templateUrl: settings.STATIC_URL + 'pages/partials/formulario.html',
                controller: 'Index.Formulario'
            });
    }]);

})();
