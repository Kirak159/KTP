
let foldBtns=document.getElementsByClassName("btn");

for(let i = 0 ; i < foldBtns.length; i++)
{
    foldBtns[i].addEventListener("click",function(event)
    {
        if (event.target.parentElement.className =="one-post folded")
        {
            event.target.parentElement.className="one-post";
            event.target.innerHTML="Свернуть";
        }
        else
        {
            event.target.parentElement.className="one-post folded";
            event.target.innerHTML="Развернуть";
        }
    });
}