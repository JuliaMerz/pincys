/*
 * Pincy's (Pinterest + Macy's) Chrome Extension
 */

  
var pincys = {
  button:  "<button class=\"pincysButton ButtonBase btn\"><em class=\"pincysEM\"></em><span class=\"accessibilityText\">Search on Macy's</span></button>",

  suggestionLoader:  function() {
    var url = $(this).parent().parent().children(".pinHolder").children().attr("href");
    $(this).addClass("active")
    var pinid = url.split("/")[2];
    console.log(pinid);
    console.log(this);

    var description = $(this).parent().parent().parent().children(".pinMeta").children(".pinDescription").html();
    var picURL = $(this).parent().parent().children(".pinHolder").children("a").children("div").children("img").attr("src");
    console.log(description);
    console.log(picURL);

    var target = $(this).parent().parent().parent().parent().parent();
    var top = target.css("top");
    var left = target.css("left");
    $.post(chrome.extension.getURL("index.html"), {id: pinid, description: description, picurl: picURL}, function(data) {console.log(data); 
    //$.get(chrome.extension.getURL("index.html"),  function(data) {console.log(data); 
      console.log($(".pincysButton.active"));
      $(document).mouseup(function (e)
        {
          var container = $(".id23");

          if (!container.is(e.target) // if the target of the click isn't the container...
            && container.has(e.target).length === 0) // ... nor a descendant of the container
          {
          container.hide();
          }
        });


      console.log(target);
      var topDist = parseInt(top) + 100;
      var topDistance = topDist+"px";
      console.log("Left distance initial: "+left+" Also: " + parseInt(left));
      if(left == "0px"){
        var leftDist = parseInt(left) + 325;
      }else{
        var leftDist = parseInt(left) - 185;
      }
      console.log("Left distance final: "+leftDist);
      var leftDistance = leftDist + "px";
      console.log(topDistance);
      console.log(leftDistance);
      $("body").append(data);
      $(".id23").tinycarousel();
      $(".id23").css("top", topDistance).css("left", leftDistance).show();
      //.mouseout(function() {
      //  console.log(this);
      //  $(this).hide();
      //  $(this).parent().children(".pincysButton.active").removeClass(".active");
        });//});


  },

  loadButtons: function(){
    var imageURL = chrome.extension.getURL("images/pincysButton.png");
    $(".repinSendButtonWrapper").append(pincys.button);
    $(".pincysButton em").css("background-image", "url("+imageURL+")")
      .parent().click(pincys.suggestionLoader);
    $(".item").addClass("loaded");
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
