   $(document).ready(function(){
   $("#comment_form  button").click(function(){
       
       var nick=$('input#id_nick').val();
       var message=$('textarea#id_message').val();
       var slug=$("#slug").attr('class');
       alert(slug);
       alert(nick);
       alert(message);

       saveComment(slug,message,nick);
   });
   
    function saveComment(slug,message,nick){
	    $.ajax({
	    url:"/save/comment/",
	    type:"post",
	    data:{slug:slug,message:message,nick:nick},
	    error:function(){alert('!!!');},
		done:function() {
		      alert(slug);
		   },
	    });
	      }
          });
