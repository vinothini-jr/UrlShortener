const text='SHORTENER';
var count=0;
var index=0;
var letter='';
(function type(){
  if(count == text.length){
   count=0;
  }
  letter=text.slice(0,++index);
  var t=document.getElementById('typing');
  console.log(t);
  document.getElementById('typing').textContent=letter;
  if (letter.length==text.length){
    count++;
    index=0;
}
setTimeout(type,400);
})();


