let data = null;

console.log("content script!!!!")
chrome.storage.local.get(["repData"],result => {
  if ( ! result.repData ) {
    navigator.geolocation.getCurrentPosition(position => {
      const req = new XMLHttpRequest();
      req.onload = function() {
        const repData = JSON.parse(this.responseText);
        chrome.storage.local.set({repData},() => {
          sendToServer(repData);
        });
      };
      req.open("GET",`https://api.geocod.io/v1.7/reverse?q=${position.coords.latitude},${position.coords.longitude}&fields=cd&api_key=2f0fb3787007bde333e78bb838bfeb66362d29d`);
      req.send();
    });
  } else {
    sendWithRepData(result.repData);
  }
});

function sendWithRepData(repData) {
  const repBio = repData.results[0].fields.congressional_districts[0].current_legislators[0].bio;
  const repName = `${repBio.first_name} ${repBio.last_name}`;
  setTimeout(() => {
    const content = document.body.innerText;
    const req = new XMLHttpRequest();
    req.onload = function() {
      data = JSON.parse(this.responseText);
    };
    req.open("POST",`http://127.0.0.1:5000/req?name=${encodeURIComponent(repName)}`);
    req.send(JSON.stringify({content}));
  },1000);
}

chrome.runtime.onMessage.addListener(function(message,sender,sendResponse) {
  sendResponse(data);
});