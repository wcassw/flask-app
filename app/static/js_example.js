function openModal() {
	document.getElementById('signup-modal').style.display = "block";
 }

window.onclick = function(event) {
	if (event.target == document.getElementById('signup-modal')) {
		document.getElementById('signup-modal').style.display = "none";
	}
}
