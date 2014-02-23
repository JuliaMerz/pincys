/*
 * Pincy's (Pinterest + Macy's) Chrome Extension
 */
var pincysButton = "<button class=\"pincysButton ButtonBase btn\"><em class=\"pincysEM\"></em><span class=\"accessibilityText\">Search on Macy's</span></button>";

  
var pincys = {
  loadButtons: function(){
    var imageURL = chrome.extension.getURL("images/pincysButton.png");
    $(".repinSendButtonWrapper").append(pincysButton);
    $(".pincysButton em").css("background-image", "url("+imageURL+")")
      .parent().click(function(event) {
        alert("clicked");
      });
  }
}

$(document).ready( function(){
  console.log("So jquery works...");
  pincys.loadButtons();
});

document.addEventListener('DOMContentLoaded', function () {
  console.log("THIS PART IS NOW RUNNING!");
    pincys.loadButtons();
});
