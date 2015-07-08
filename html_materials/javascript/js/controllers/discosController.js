app.controller('DiscosController', ['$scope', function($scope) {
  $scope.page=0;
  $scope.hideMoreButton=false;

  $scope.discos = [{
    author: "Miss Caffeina",
    id : "7xKn54vuBZarFs70PFBtAu",
    image: "978262d4c3094870bf926b1ffe8ae77551b75f43",
    name : "De polvo y flores",
    type : "album",
    uri: "spotify:album:7xKn54vuBZarFs70PFBtAu",
    tracks: ["Tormento",
             "Disfraces",
             "Gigantes",
             "Hielo T",
             "Luciernaga",
             "MM",
             "Venimos",
             "Superhéroe",
             "No mienten",
             "San Francisco",
             "Modo avión",
             "19"]
  }, {
    author: "Miss Caffeina",
    id : "5rapGUcV8dZrJkje17NMxM",
    image : "eab525bd25449088895a740c36879119b2a2d275",
    name : "Imposibilidad Del Fenomeno",
    type : "album",
    uri: "spotify:album:5rapGUcV8dZrJkje17NMxM",
    tracks: ["Capitan",
             "Ley De Imposibilidad Del Fenomeno",
             "Cabaret",
             "N=3",
             "Mecanica Espiral",
             "Mi Rutina Preferida",
             "La Guerra",
             "Lisboa",
             "Ley De Gravitacion Universal",
             "N=1",
             "Perfecto"]
  }, {
    author : "Miss Caffeina",
    id : "2kGVK8UutJFDznGERb8VRX",
    image : "673373c419f6cebe4769e0b59c0741f22caaeb7f",
    name : "Magnética",
    type : "album",
    uri: "spotify:album:2kGVK8UutJFDznGERb8VRX",
    tracks: ["Ley De Gravitación Universal",
             "Mecánica Espiral",
             "Mi Rutina Preferida",
             "Caleidosferico",
             "Príncipes Del Rock'n Roll",
             "3000",
             "Otoño Y Mariposas"]
  }, {
    author : "Supersubmarina",
    id : "49Av22K1Doe8E6AfQrdWeI",
    image : "009d225ae762f640e01b6be28feb4eef798d03d2",
    name : "BCN",
    type : "album",
    uri: "spotify:album:49Av22K1Doe8E6AfQrdWeI",
    tracks: ["Cometas - BCN",
             "Santacruz - BCN",
             "Ola de Calor - BCN",
             "Cancion de Guerra - BCN",
             "Para Dormir Cuando No Estes - BCN",
             "Ana - BCN",
             "El Baile de los Muertos - BCN",
             "Tu Saeta - BCN",
             "Eres - BCN",
             "Centro de Atencion - BCN",
             "Emperatriz - BCN",
             "Electrico - BCN",
             "Hogueras - BCN",
             "LN Granada - BCN",
             "El Encuentro - BCN",
             "Kevin Mc Alister - BCN",
             "Hermetica - BCN",
             "XXI - BCN",
             "Niebla - BCN",
             "Cientocero - BCN",
             "De las Dudas Infinitas - BCN",
             "OCB - BCN",
             "Supersubmarina - BCN",
             "Tecnicolor - BCN",
             "Elastica Galactica - BCN",
             "Puta Vida - BCN",
             "En Mis Venas - BCN",
             "Gin Tonic - BCN"]
  }, {
    author : "Supersubmarina",
    id : "1H12cM0oy1TMb5snNa040x",
    image: "1b5517d8bb5b79547f614e04263a9fa1d11fb1e7",
    name : "Viento de Cara",
    type : "album",
    uri: "spotify:album:1H12cM0oy1TMb5snNa040x",
    tracks: ["Viento de Cara",
             "Algo Que Sirva Como Luz",
             "De Doce a Doce y Cuarto",
             "Arena y Sal",
             "Extrema Debilidad",
             "Inestable",
             "Hasta Que Sangren",
             "Furia",
             "Enemigo Yo",
             "Samurái",
             "El Mañana"]
  }, {
    author : "Supersubmarina",
    id : "6F0M6o2oFl8pf52SbckNWf",
    image: "0bcbf4d74ebbdb2f6a93b4651c948a62fbd3c54c",
    name : "Santacruz",
    type : "album",
    uri: "spotify:album:6F0M6o2oFl8pf52SbckNWf",
    tracks: ["Cancion De Guerra",
             "Santacruz",
             "Hermetica",
             "En Mis Venas",
             "Tu Saeta",
             "Para Dormir Cuando No Estes",
             "El Baile De Los Muertos",
             "De Las Dudas Infinitas",
             "Tecnicolor",
             "Cometas",
             "Hogueras"]
  }, {
    author : "Supersubmarina",
    id : "3LYJiRx2vxocmtxikxcnKN",
    image: "8cec8aa7feb45c840a2bcd3fb51e907f58c0fd44",
    name : "Electroviral",
    type : "album",
    uri: "spotify:album:3LYJiRx2vxocmtxikxcnKN",
    tracks: ["Magia Electroviral",
             "Electrico",
             "Niebla",
             "Supersubmarina",
             "Ana",
             "LN Granada",
             "Chas! Y Aparezco A Tu Lado",
             "Cientocero",
             "XXI",
             "Elastica Galactica",
             "Ola De Calor",
             "Centro De Atencion",
             "Eres"]
  }, {
    author: "Love of Lesbian",
    id : "5fP8Ww6lVCwOaqcwSy1ae8",
    image : "0aea16ef1401c0bf4a1ff6ddad0f6859fabab3f1",
    name : "La noche eterna. Los días no vividos",
    type : "album",
    uri: "spotify:album:5fP8Ww6lVCwOaqcwSy1ae8",
    tracks: ["La noche eterna",
             "Los seres únicos",
             "Si tu me dices Ben, yo digo Affleck",
             "Nada",
             "Belice",
             "Pizzigatos",
             "667",
             "Cínicamente muertos",
             "Orden de desahucio en mi menor",
             "Oniria e insomia",
             "Nadie por las calles",
             "El hambre invisible",
             "Wio, antenas y pijamas",
             "Si salimos de esta",
             "Tercero segunda",
             "Los días no vividos",
             "Radio Himalaya",
             "Los toros en la Wii - Fantástico"]
  }, {
    author: "Love of Lesbian",
    id : "1vvfLVVcU1o8sPMq25CxpF",
    image : "d8f5c8a1130550e05ebdbbb3950d404bddc6ae34",
    name : "1999 (o como generar incendios de nieve con una lupa enfocando la luna)",
    type : "album",
    uri: "spotify:album:1vvfLVVcU1o8sPMq25CxpF",
    tracks: ["Alli donde soliamos gritar",
             "Club de fans de John Boy",
             "Las malas lenguas",
             "Algunas plantas",
             "Cuestiones de familia",
             "El ectoplasta",
             "Segundo asalto",
             "Incendios de nieve",
             "1999",
             "Te hiero mucho (Historia del amante guisante)",
             "Cuando diga ya",
             "Miau",
             "La mirada de la gente que conspira",
             "2009. Voy a romper las ventanas"]
  }, {
    author: "Love of Lesbian",
    id : "2lxyia5M2yZLXpxsyWXzqV",
    image : "ac938d6e17d3d271fba0c6c04670c92411b1be36",
    name : "Cuentos Chinos para Niños del Japón",
    type : "album",
    uri: "spotify:album:2lxyia5M2yZLXpxsyWXzqV",
    tracks: ["Universos Infinitos",
             "La Niña Imantada",
             "Noches Reversibles",
             "Los Colores de una Sombra",
             "Un Día en el Parque",
             "Villancico para Mi Cuñado Fernando",
             "Shiwa",
             "Me Amo",
             "Historia de una Hache Que No Quería Ser Muda",
             "La Parábola del Tonto",
             "Momento de Reflexión #1",
             "Dios por Dios Es Cuatro",
             "Moment de Reflexió #2",
             "Shiwa (Tot a Zen)"]
  }, {
    author: "Love of Lesbian",
    id : "7D3CvFm06gxWNtnx83FwAF",
    image:  "31ddfde62644518c71e778da7cd843c2d5a02919",
    name : "Maniobras de Escapismo",
    type : "album",
    uri: "spotify:album:7D3CvFm06gxWNtnx83FwAF",
    tracks: ["Carta a Todas Tus Catástrofes",
             "Maniobras de Escapismo",
             "Domingo Astronómico",
             "Mi Personulidad",
             "Houston, Tenemos un Poema",
             "Mi Primera Combustión",
             "Música de Ascensores",
             "Marlene, La Vecina del Ártico",
             "Los Niños del Mañana",
             "Me Llaman Octubre",
             "Limousinas",
             "Mon petit cabroin"]
  }, {
    author: "Love of Lesbian",
    id : "3i1B0y1K4lglRORuV6D8sf",
    image : "99096e3a251f069214ba6f9b42823f89de47e8c6",
    name : "Is It Fiction?",
    type : "album",
    uri: "spotify:album:3i1B0y1K4lglRORuV6D8sf",
    tracks: ["Shine It",
             "All These Days",
             "Evasive",
             "A Day In The Park",
             "Lou Reed In My City",
             "Stupid At All",
             "Move On",
             "Wasted Days",
             "Transexual Soul",
             "U",
             "Make Up",
             "Is It Fiction"]
  }, {
    author: "Love of Lesbian",
    id : "5tvMOJXJFXQxrRLK7o3YvZ",
    image : "97de625e3e92f53203a1baed76edcc6bb90512a3",
    name : "Ungravity",
    type : "album",
    uri: "spotify:album:5tvMOJXJFXQxrRLK7o3YvZ",
    tracks : ["Hi to the Next Times",
        "Satellites",
        "Scape",
        "Galaxy of Loneliness",
        "Wall Poetry",
        "Love Song Nº 79.899",
        "Life on Cinemascope",
        "White Day",
        "Radio in My Brain",
        "Macba Girl",
        "Galaxy of Drawning Men",
        "Ungravity (Still Amazed by the Stars) - Bonus Track"
        ]

  }];

  $scope.MoreDiscos = function(){
    $scope.hideMoreButton = $scope.page +1 == ($scope.discos.length/3) >>0 ? true : false;
    $scope.page = $scope.page < ($scope.discos.length/3) >>0 ? ($scope.page+1) : 0;
    $scope.show = $scope.discos.slice(3*$scope.page, 3*$scope.page+3);
  }


  $scope.show = $scope.discos.slice(3*$scope.page, 3*$scope.page+3)

}]);