 var app = angular.module("MusicApp",[]);

 app.config( ['$compileProvider',
    function( $compileProvider )
    {   
        $compileProvider.aHrefSanitizationWhitelist(/^\s*(spotify):/);

    }]);