$(document).ready(function()){
  const inputs=document.querySelectorAll(`input.star`);
  inputs.forEach(input=>{input.addEventListener('click',rate);});
  function rate(){
    const rate=$(this).attr("data-value");
    const cat=$(this).attr("data-cat");
    const page=$(this).attr("data-page");
    $.get('/courses/rating/'),{category_name:cat,page:page},fuction(){
      
    }
   }
}
