/*
 * Pincy's (Pinterest + Macy's) Chrome Extension
 */

  
var pincys = {
  button:  "<button class=\"pincysButton ButtonBase btn\"><em class=\"pincysEM\"></em><span class=\"accessibilityText\">Search on Macy's</span></button>",

  suggestionLoader:  function() {
    var url = $(this).parent().parent().children(".pinHolder").children().attr("href");
    var pinid = url.split("/")[2];
    console.log(pinid);
    $(this).append($.get("http://www.pincy.co:5000/getSuggestions/"+pinid));
  },

  loadButtons: function(){
    var imageURL = chrome.extension.getURL("images/pincysButton.png");
    $(".repinSendButtonWrapper").append(pincys.button);
    $(".pincysButton em").css("background-image", "url("+imageURL+")")
      .parent().click(pincys.suggestionLoader);
    $(document).on("DOMNodeInserted","div[class='item ']", pincys.loadButton);
    $(document).on("DOMNodeInserted","div[class='ajax HomePage Module']", pincys.loadGroupButtons);
  },

  loadButton: function() {
    console.log("Load Button");
    //console.log("attempt");
    //if($(this).hasClass("item")){
    //console.log(this);
    var imageURL = chrome.extension.getURL("images/pincysButton.png");
    $(this).addClass("loaded");
    $(this).children().children().children(".pinImageActionButtonWrapper")
      .children(".repinSendButtonWrapper").append(pincys.button)
      .children(".pincysButton").children(".pincysButton em")
      .css("background-image", "url("+imageURL+")")
      .parent().click(pincys.suggestionLoader);
    //}
  },

  loadGroupButtons: function() {
    console.log("Big attempt");
    console.log(this);
    var imageURL = chrome.extension.getURL("images/pincysButton.png");
    $(this).addClass("loaded");
    var stuff = $(this).children().children().children("div").children(".padItems")
        .children().children().children().children(".pinImageActionButtonWrapper")
        .children(".repinSendButtonWrapper");
    console.log(stuff);
    stuff.append("<b></b>");
  }

}

$(document).ready( function(){
  console.log("So jquery works...");
  pincys.loadButtons();
});

/*document.addEventListener('DOMContentLoaded', function () {
  console.log("THIS PART IS NOW RUNNING!");
    pincys.loadButtons();
});*/
