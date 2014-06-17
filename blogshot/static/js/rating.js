$(document).ready(function(){
    $("#bottom_wrapper > #rating img").click(function(){
      var clickId=this.id;
      var slug=$(this).parent().parent().parent().parent().attr('id');
   EditRating(clickId,slug);
   });
  
   function EditRating(funct,slug){
      switch(funct){
	 case 'plus':
	    $.ajax({
	    url:"/save/post_rating",
	    type:"post",
	    data:{slug:slug,funct:'plus',},
	    error:function(){alert('опаньки, ошибочка...');},
	    success:function(rating) {
		    if (rating!='null'){
		       $('#bottom_wrapper .num').text(rating);
		  };
		      
		  }
	    }); break;
	 case 'minus':
	    $.ajax({
	       url:"/save/post_rating",
	    type:"post",
	    data:{slug:slug,funct:'minus'},
	    error:function(){alert('опаньки, ошибочка...');},
	    success:function(rating) {
		      if (rating!='null'){
			 $('#bottom_wrapper .num').text(rating);
		      }
		   }
	    }); break;
	    }
   }
    clik_consumer($("#comment_wrapper  #rating_com  img"));
});
