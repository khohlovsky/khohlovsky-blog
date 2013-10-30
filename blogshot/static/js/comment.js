   $(document).ready(function(){
   $("#comment_form  button").click(function(){
       
       var nick=$('input#id_nick').val();
       var message=$('textarea#id_message').val();
       var slug=$("#slug").attr('class');
       if (nick.length<6){
           $('input#id_nick').val('!');
           }
       saveComment(slug,message,nick);
   });
   
    function saveComment(slug,message,nick){
	    $.ajax({
	    url:"/save/comment/",
	    type:"post",
	    data:{slug:slug,message:message,nick:nick},
		success:function(da) {
            $('#comment_list').empty();
            $('#comment_list').append(da);
            clik_consumer($("#comment_wrapper  #rating_com  img"));}
	    });
	      }
          });
