   $(document).ready(function(){
   $("#comment_form  button").click(function(){
       
       var nick=$('input#id_nick').val();
       var message=$('textarea#id_message').val();
       var id=$("#slug").attr('class');
       alert(id);
       alert(nick);
       alert(message);

       saveComment(id,message,nick);
   });
   
    function saveComment(id,message,nick){
	    $.ajax({
	    url:"/save/comment",
	    type:"post",
	    data:{id:id,message:message,nick:nick},
	    error:function(){alert('опаньки, ошибочка...');},
		done:function(html) {
		      $("#comment_wrapper").html(html);
		   }
	    });
	      }
          });
