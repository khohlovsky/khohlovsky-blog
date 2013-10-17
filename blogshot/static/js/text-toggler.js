$(document).ready(function(){
   var $font=$('.description p');
   var size=parseFloat($font.css('fontSize'),10);
   defSize=size;
   if ($.session("size")){
      size=$.session("size");
      $font.css('fontSize',size+'px');
   }
   $('#text_toggler > a').click(function(){
      switch (this.id){
	 case 'less':
	    size /= 1.1; break;
	 case 'def':
	    size = defSize; break;
	 case 'bigger':
	    size *= 1.1; break;
      }
      // 	 if (this.id=='less'){
      // 	    size /= 1.2;
      // 	    }
      // 	 if (this.id=='bigger'){
   // 	    size *= 1.2;
   // 	    }
   // 	 if (this.id=='def'){
      // 	    size=defSize;
      // 	    }
      $.session("size",size);
      size=$.session("size");
      $font.css('fontSize',size+'px');
   });
 
   
});
