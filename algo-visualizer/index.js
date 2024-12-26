$(document).ready(function() {
let L =[1,2,3,4,5,6,7,8,9,100]
animateArray(L,3)

});

function animateArray(L,index=2){
    var i = 0
    var html = ""
    L.forEach(e => {
        cls =(i==index)?"cell active" :"cell"
        html += '<div class="'+cls+'">'
        html+='<div>'+ e + '</div>\n'
           html+='<div>'+ i + '</div>\n'
        
        html+='</div>\n'
     
        i++
    });
    console.log(html)
    $("#code").html(html)
}