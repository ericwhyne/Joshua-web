app.controller("myTranslationCtrl", function($scope, $http) {
	$scope.last_text="";
	$scope.orig_text = "";
	$scope.numCharcters  = function() {return  $scope.orig_text.length;};
	$scope.clear = function() {$scope.orig_text = ""; 
	$scope.translated_text=""; ""
	
	};


	$scope.translate = function(){

		if($scope.last_text!=$scope.orig_text)
		{
			console.log("last_text.length"+$scope.last_text.length+"this text length"+$scope.orig_text.length);
			
			//10.1.70.133:873
			var urlStr=$("input#api_url").val()+'?format=json&orig_text="'+$scope.orig_text+'"';

			console.log("requesting translation using api"+urlStr);
			$http.get(urlStr).
			success(function(data, status, headers, config) {
				// this callback will be called asynchronously
				// when the response is available
				$scope.translated_text=data.translations[0].translated_text;
				//  alert("get success");
			}).
			error(function(data, status, headers, config) {
				// called asynchronously if an error occurst
				// or server returns response with an error status.
				alert("Translate failed, please make sure server is up");
			});
			$scope.last_text=$scope.orig_text;
		}
		

	} ;

}); 
