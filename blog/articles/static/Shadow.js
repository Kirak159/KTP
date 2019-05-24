$(document).ready(function(){
    $('.one-post').hover(function(event) {
        console.log('Навели');
        console.log(event.currentTarget);
    },  function(event){
        console.log('Вывели')
    });
});

$(document).ready(function(){
    $('.one-post').hover(function(event) {
        $(event.currentTarget).find('.one-post-shadow').animate({opacity:'0.1'},300);
    },  function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity:'0'},300);
    });
});

$(document).ready(function(){
    $('.logo-img').hover(function(event){
        $(event.currentTarget).find('.logo').animate({width:'100%',height: 'auto'},300)
    }, function(event){
        $(event.currentTarget).find('.logo').animate({width:'90%',height: 'auto'},300)
    })

});
