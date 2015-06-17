(function(){

    var FIELDS = {
        phone_number: 'Número de teléfono',
        city: 'Ciudad',
        name: 'Nombre',
        content: 'Comentarios',
        address: 'Dirección',
        email: 'E-mail'
    };

    var MONTHS = [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre'
    ];

    var Index = angular.module('Index', ['ui.bootstrap', 'ui.router', 'ngCookies']);

    Index.controller('Index.Main', ['$rootScope', '$state', '$http', '$interval', '$timeout', 'Settings', '$modal',
                     function($rootScope, $state, $http, $interval, $timeout, settings, $modal) {
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
                var url = '/replacements/cheap/' + id;
                console.log('Accediendo a ' + url);
                $http
                    .get(url)
                    .success(function(data) {
                        $rootScope.modalState = 'closed';
                        $rootScope.currentPromo = data;
                        if ($rootScope.modalState != 'opened') {
                            $rootScope.modalState = 'opened';
                            console.log("opening ...");
                            var instance = $modal.open({
                                keyboard: true,
                                backdrop: true,
                                templateUrl: 'display.promo.html',
                                windowClass: 'form-dialog popup',
                                scope: $rootScope,
                                controller: ['$scope', '$modalInstance',
                                    function($scope, $modalInstance){
                                        $scope.goPromo = function(promo){
                                            $modalInstance.close();
                                            $state.go('formulario',
                                                {defaultText: "Buenos días.\n\nEstoy interesado en adquirir: \"" + promo.product +
                                                              "\" para marca \"" + promo.brand +  "\" y modelo \"" + promo.model + "\"."});
                                        };
                                    }]
                            });
                            instance.result.then(function(){
                                $rootScope.modalState = 'closed';
                            }, function(){
                                $rootScope.modalState = 'closed';
                            });
                        }
                    });
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
            });
        $rootScope.form_reel = {
            "images_list": [],
            "code": "reelform",
            "name": "Reel del Form",
            "description": "Reel del formulario",
            "link_default": "",
            "link_prevails": true
        };
        $http
            .get('/ads/reel/reelform', {})
            .success(function(data){
                $rootScope.form_reel = data;
                $rootScope.form_reel.current = null;
                var index = 0;
                $interval(function(){
                    index++;
                    if (index == $rootScope.form_reel.image_list.length) {
                        index = 0;
                    }
                    $rootScope.form_reel.current = $rootScope.form_reel.image_list[index];
                }, 4000);
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
    Index.controller('Index.Blog', ['$scope', '$state', '$http', function($scope, $state, $http){
        var date = new Date();
        $scope.goList = function(year, month) {
            console.log("Going to blog list " + year + '/' + month);
            $state.go('blog.list', {
                month: month,
                year: year
            });
        };
        $scope.errorOnPeriods = false;
        $scope.loadingPeriods = true;
        $scope.monthName = function(month) {
            return MONTHS[month - 1];
        };
        $http
            .get('/blog/summary', {})
            .success(function(data){
                $scope.loadingPeriods = false;
                if (!data) {
                    data = [
                        {
                            created_year: date.getFullYear(),
                            created_month: date.getMonth() + 1,
                            entries_month: 0
                        }
                    ]
                }
                var last = data[data.length - 1];
                $scope.periods = data;
                $scope.errorOnPeriods = false;
                $scope.goList(last.created_year, last.created_month);
            })
            .error(function(data, status){
                $scope.loadingPeriods = false;
                $scope.errorOnPeriods = true;
            });
    }]);
    Index.controller('Index.Blog.One', ['$scope', '$state', '$stateParams', '$http', '$sce',
                                        function($scope, $state, $stateParams, $http, $sce){
        console.log('displaying blog entry: ' + $stateParams.id);
        $scope.entry = null;
        $scope.errorOnEntry = false;
        $scope.loadingEntry = true;
        $http
            .get('/blog/entry/' + ($stateParams.id || 0), {})
            .success(function(data){
                $scope.entry = data;
                $scope.entry.content = $sce.trustAsHtml($scope.entry.content);
                console.log($scope.entry);
                $scope.loadingEntry = false;
                $scope.errorOnEntry = false;
            })
            .error(function(data, status){
                $scope.errorOnEntry = true;
                $scope.loadingEntry = false;
            });
    }]);
    Index.controller('Index.Blog.List', ['$scope', '$state', '$stateParams', '$http',
                                         function($scope, $state, $stateParams, $http){
        $scope.goOne = function(id) {
            console.log('going to blog entry: ' + id);
            $state.go('blog.one', {
                id: id
            });
        };
        $scope.entriesList = [];
        $scope.errorOnEntriesList = false;
        $scope.loadingEntriesList = true;
        console.log("Displaying: " + $stateParams.year + '/' + $stateParams.month);
        $http
            .get('/blog/entries/' + ($stateParams.year || 2000) + '/' + ($stateParams.month || 0), {})
            .success(function(data){
                $scope.entriesList = data;
                $scope.errorOnEntriesList = false;
                $scope.loadingEntriesList = false;
            })
            .error(function(data, status){
                $scope.errorOnEntriesList = true;
                $scope.loadingEntriesList = false;
            });
    }]);
    Index.controller('Index.Formulario', ['$rootScope', '$scope', '$http', '$state', '$stateParams', '$cookies', 'Settings',
                                          function($rootScope, $scope, $http, $state, $stateParams, $cookies, settings){
        var tracking = $stateParams.tracking;
        var defaultText = $stateParams.defaultText || '';
        $scope.success = false;
        $scope.form = {
            name: '',
            email: '',
            address: '',
            phone_number: '',
            city: '',
            content: defaultText,
            tracking: tracking
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
            'MEDIA_URL': '/media/',
            'CONTACT_URL': '/contact/'
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
            .state('blog.one', {
                params: ['id'],
                templateUrl: settings.STATIC_URL + 'pages/partials/blog-one.html',
                controller: 'Index.Blog.One'
            })
            .state('blog.list', {
                params: ['year', 'month'],
                templateUrl: settings.STATIC_URL + 'pages/partials/blog-list.html',
                controller: 'Index.Blog.List'
            })
            .state('formulario', {
                params: ['tracking', 'defaultText'],
                templateUrl: settings.STATIC_URL + 'pages/partials/formulario.html',
                controller: 'Index.Formulario'
            });
    }]);

})();
