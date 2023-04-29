var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i < foldBtns.length; i++)
{
	foldBtns[i].addEventListener("click", function(e) 
	{ 
		if (e.target.className == "fold-button") 
		{
			Array.from(event.target.parentElement.getElementsByClassName('visible')).forEach(item => 
				{item.className = "hide";});
			e.target.innerHTML = "Развернуть";
			e.target.className = "fold-button-folded";
		}
		else if (e.target.className == "fold-button-folded") 
		{
			Array.from(event.target.parentElement.getElementsByClassName('hide')).forEach(item => 
				{item.className = "visible";});
			e.target.innerHTML = "Свернуть";
			e.target.className = "fold-button";
		}

	});
}
