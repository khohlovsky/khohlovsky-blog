function EditRatingCom(funct,id){
      switch(funct){
	 case 'plus':
	    $.ajax({
	       url:"/save/comment_rating",
	    type:"post",
	    data:{id:id,funct:'plus',},
	    error:function(){alert('опаньки, ошибочка...');},
		   success:function(rating) {
		      if (rating!='null'){
			 $('div[id='+id+'] .num').text(rating);
		      };
		      
		   }
	    }); break;
	 case 'minus':
	    $.ajax({
	       url:"/save/comment_rating",
	    type:"post",
	    data:{id:id,funct:'minus'},
	    error:function(){alert('опаньки, ошибочка...');},
		   success:function(rating) {
		      if (rating!='null'){
			 $('div[id='+id+'] .num').text(rating);
		      }
		   }
	    }); break;
      }}

function clik_consumer(selector){
    selector.click(function(){
            var clickId=this.id;
            var id=$(this).parent().parent().attr('id');
            var th=$(this);
        EditRatingCom(clickId,id,th);
   });
 }

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
