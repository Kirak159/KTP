$(document).ready(function(){
    let yPosition,
        scrolled=0,
        $parallaxElements=$('.logo-parallax img');
    $(window).scroll(function(){
        scrolled=$(window).scrollTop();
        for(let i=0;i<$parallaxElements.length;i++){
            yPosition=(scrolled*0.15*(i+1));
            $parallaxElements.eq(i).css({top:yPosition});
        }
    });
});

$(document).ready(function(){
    let yPosition,
        scrolled=0,
        $parallaxElements=$('.logo-parala img');
    $(window).scroll(function(){
        scrolled=$(window).scrollTop();
        for(let i=0;i<$parallaxElements.length;i++){
            yPosition=(scrolled*0.15*(i+1));
            $parallaxElements.eq(i).css({top:yPosition});
        }
    });
});