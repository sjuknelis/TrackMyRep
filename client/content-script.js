let data = null;

console.log("content script")

setTimeout(() => {
  const content = document.body.innerText;
  const req = new XMLHttpRequest();
  req.onload = function() {
    data = JSON.parse(this.responseText);
  };
  req.open("POST","http://127.0.0.1:5000/req");
  req.send(JSON.stringify({content}));
},1000);

chrome.runtime.onMessage.addListener(function(message,sender,sendResponse) {
  sendResponse(data);
});