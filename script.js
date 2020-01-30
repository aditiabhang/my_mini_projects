const canvas = document.getElementById("canvas");
// selecting canvas elements 

const ctx = canvas.getContext("2d");
//rendering context - allows us to access the range of drawn functions, to manipulate what is on the canvas.

//------------------------------------------------
// ctx.fillText("Canvas text!", 100, 50)

// ctx.fillStyle = "#EEEDDD";
// ctx.fillRect(0,0, 50, 50)


// ctx.fillStyle = "red";
// ctx.beginPath();
// ctx.moveTo(canvas.width/2, canvas.height/2);
// ctx.lineTo(250, 50);
// ctx.lineTo(250, 100);
// ctx.closePath();
// ctx.stroke(); 
// //to make solid color > ctx.fill();
//------------------------------------------------

const reader = new FileReader();

const img = new Image();

const uploadImage = e => {
    //console.log(e) - example to view the file data 
    reader.onload = () => {
        img.onload = () => {
            canvas.width = img.width;
            canvas.height = img.height;
            ctx.drawImage(img, 0,0)
            //console.log(imageData) - to view data in console
        }
        img.src = reader.result;
    }
    reader.readAsDataURL(e.target.files[0])
    //console.log(reader) - to have the value of the file reader, instead of null in result.
}

// F A C T:
// When we open the console ImageData > we find data of 180000 pixel values. Whereas our size of image is 150 x 300 = 45000, the resulting pixel is size 4x more than it. 
// Reason: Because an image has 4 factors, RBG and alpha(transparency) value.

const imageLoader = document.getElementById("uploader");
imageLoader.addEventListener("change", uploadImage);

const greyscale = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        const grey = data[i]*0.21 + data[i+1]*0.71 + data[i+2]*0.07;
        data[i] = grey;     //red value
        data[i+1] = grey;   //green value
        data[i+2] = grey;   //blue value
    }
    ctx.putImageData(imageData, 0,0);
    //console.log(imageData)      //In the console > data, we find the RGB@ all B as 255.
}

const sepia = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        const grey = data[i]*0.21 + data[i+1]*0.71 + data[i+2]*0.07;
        data[i] = grey + 95;     //red value
        data[i+1] = grey + 58;   //green value
        data[i+2] = grey;   //blue value
    }
    ctx.putImageData(imageData, 0,0);
}

const invert = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        data[i] = 255-data[i];
        data[i+1] = 255-data[i+1];
        data[i+2] = 255-data[i+2];
    }
    ctx.putImageData(imageData, 0,0);
}

const rbg = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        data[i] = data[i];
        data[i+1] = data[i+2];
        data[i+2] = data[i+1];
    }
    ctx.putImageData(imageData, 0,0);
}

const bgr = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        data[i] = data[i+2];
        data[i+1] = data[i+1];
        data[i+2] = data[i];
    }
    ctx.putImageData(imageData, 0,0);
}

const gbr = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        data[i] = data[i+1];
        data[i+1] = data[i+2];
        data[i+2] = data[i];
    }
    ctx.putImageData(imageData, 0,0);
}

const grb = () => {
    const imageData = ctx.getImageData(0,0, canvas.width, canvas.height);
    const data = imageData.data
   
    for(let i=0; i<data.length; i += 4) {
        data[i] = data[i+1];
        data[i+1] = data[i];
        data[i+2] = data[i+2];
    }
    ctx.putImageData(imageData, 0,0);
}

const clearChanges = () => {
    //console.log(reader)
    img.src = reader.result;
}

document.querySelectorAll("button")[0].addEventListener("click", greyscale);
document.querySelectorAll("button")[1].addEventListener("click", sepia);
document.querySelectorAll("button")[2].addEventListener("click", invert);
document.querySelectorAll("button")[3].addEventListener("click", rbg);
document.querySelectorAll("button")[4].addEventListener("click", bgr);
document.querySelectorAll("button")[5].addEventListener("click", gbr);
document.querySelectorAll("button")[6].addEventListener("click", grb);
document.querySelectorAll("button")[7].addEventListener("click", clearChanges);