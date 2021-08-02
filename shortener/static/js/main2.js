var copied=document.getElementById('copy-btn');
 console.log(copied)
copied.addEventListener('click',function(event){
    var data=copied.getAttribute('data')
    navigator.clipboard.writeText(data)
    copied.textContent="copied"
})