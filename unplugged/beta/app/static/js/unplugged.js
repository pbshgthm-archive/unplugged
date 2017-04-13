	
//----------------SMOOTH SCROLLING EFFECT BEGIN-----------------------------------

  $(document).ready(function(){
  $("a").on('click', function(event) {

    

    this_page=false;
    all_hash=document.querySelectorAll('*[id]')
    for(var i=0;i<all_hash.length;i++){
      if("#"+all_hash[i].id==this.hash)
        {this_page=true;break;}
    }
    
    // Make sure hash is in this page before overriding default behaviour
    if (this_page) {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 2000, function(){
   
        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });
});

///////////////////////





//----------------SMOOTH SCROLLING EFFECT END-----------------------------------


  
//----------------DISCOVER CHANGE BEGIN-----------------------------------

function discover(item) {
    document.getElementsByClassName('discover-people')[0].style.display="none";
    document.getElementsByClassName("discover-circles")[0].style.display="none";
    document.getElementsByClassName('discover-topic')[0].style.display="none";
    document.getElementsByClassName(item)[0].style.display="inline";
  }


//----------------DISCOVER CHANGE END-----------------------------------
