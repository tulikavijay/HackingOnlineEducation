// $(document).ready(function()){
//   const inputs=document.querySelectorAll(`input.star`);
//   inputs.forEach(input=>{input.addEventListener('click',rate);});
//   function rate(){
//     const rate=$(this).attr("data-value");
//     const cat=$(this).attr("data-cat");
//     const page=$(this).attr("data-page");
//     $.get('/courses/rating/'),{category_name:cat,page:page,rate:rate},fuction(data){
//       $('.desc').html(data);
//     }
//    }
// }
// $(document).ready(function(){
//   const forms=document.querySelectorAll(`form`);
//   forms.forEach(form=>{form.addEventListener('submit',rate);});
//   function rate(){
//     const page=$(this).attr("data-page");
//     const rate=$("[data-page]")
//   }
// })
$(document).ready(function(){
  const forms=document.querySelectorAll(`form`);
   forms.forEach(form=>{form.addEventListener('submit',rating);});
   var rate='';
   var cat='';
   var page='';
   $('input[type=radio]').on('click',function(){
     console.log(this);
      rate=$(this).attr("data-rate");
      cat=$(this).attr("data-cat");
      page=$(this).attr("data-page");
      $(this).closest("form").submit();
   });
   function rating(){
     console.log(rate);
         $.post('/rate/',{category_name:cat,page:page,rate:rate},function(data){
           $('.desc').html(data);
         });
   }
});
