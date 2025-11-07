

function checkboxChange(clickedBox){
    //function to ensure only one option can be selected at one time
    if(clickedBox.id == "Take-out" && clickedBox.checked){
        document.getElementById("Return").checked = false;
    } else if(clickedBox.id == "Return" && clickedBox.checked){
        document.getElementById("Take-out").checked = false;
    }

}

function startScanner() {
  const logDiv = document.getElementById('log'); //display messages to the user
  //setup the qr scanner and display video feed
  const html5QrCode = new Html5Qrcode("reader"); //will create a new object where the qr reader will appear

  //ask the browser for a list of available cameras
  //.then --> when the cameras are found run the following function...
  // cameras{} is working as an array {id:label}
  Html5Qrcode.getCameras().then(cameras => {
    //ensure cameras are working... if true
    if (cameras && cameras.length) {
        //using the first camera in the list setup with these specs
      html5QrCode.start(
        cameras[0].id,
        { fps: 10, qrbox: 250 },
        qrCodeMessage => {
            //callback function - when qr detected
          logDiv.textContent = "Scanned: " + qrCodeMessage;
        }
      );
    } else {
      logDiv.textContent = "No camera found.";
    }
  }).catch(err => {
    logDiv.textContent = "Camera access error: " + err;
  });
}



