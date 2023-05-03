let data = null;

console.log("content script!!!!")
chrome.storage.local.get(["repData"],result => {
  console.log(result.repData)
  if ( ! result.repData ) {
    navigator.geolocation.getCurrentPosition(position => {
      const req = new XMLHttpRequest();
      req.onload = function() {
        const repData = JSON.parse(this.responseText);
        console.log(repData);
        chrome.storage.local.set({repData},() => {
          sendToServer(repData);
        });
      };
      console.log(position.coords);
      //req.open("GET",`https://api.geocod.io/v1.7/reverse?q=${position.coords.latitude},${position.coords.longitude}&fields=cd&api_key=2f0fb3787007bde333e78bb838bfeb66362d29d`);
      req.open("GET",`https://api.geocod.io/v1.7/reverse?q=42.272194,-71.380446&fields=cd&api_key=2f0fb3787007bde333e78bb838bfeb66362d29d`);
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
    console.log(repBio);
    const content = document.body.innerText;
    const req = new XMLHttpRequest();
    req.onload = function() {
      data = JSON.parse(this.responseText);
    };
    req.open("POST",`http://127.0.0.1:5123/req?name=${encodeURIComponent(repName)}`);
    req.send(JSON.stringify({content}));
  },1000);
}

chrome.runtime.onMessage.addListener(function(message,sender,sendResponse) {
  sendResponse(data);
});