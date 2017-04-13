$(document).ready(function(){
  var timeoutID = null;
  function find(){
    searchString = $('#searchbar').val()
     if ( validate(searchString) === true ){
       function  performQuery(searchString){
    $.ajax({
        type: "GET",
        url: "/search",
        data: { "string": searchString },
        success: function (response){
            $( "#searchbar" ).autocomplete({
            source: response
            });
          });
        }
      });
  }
}
  $('#target').keyup(function(e)
  {
    clearTimeout(timeoutID);
    timeoutID = setTimeout(find.bind(undefined, e.target.value), 2000);
  });
  };
});
