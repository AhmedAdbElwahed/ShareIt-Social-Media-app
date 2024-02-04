const siteUrl = 'https://mysite.com:8000/';
const styleUrl = siteUrl + 'static/css/style.css';
const minWidth = 250;
const minHeight = 250;

// load CSS
const head = document.getElementsByTagName('head')[0];
const link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random() * 9999999999999999);
head.appendChild(link);

// load HTML
const body = document.getElementsByTagName('body')[0];
boxHtml = `
  <div id="bookmarklet">
    <a href="#" id="close">&times;</a>
    <h1>Select an image to bookmark:</h1>
    <div class="images"></div>
  </div>`;
body.innerHTML += boxHtml;

function bookmarkletLaunch() {
    let bookmarklet = document.getElementById('bookmarklet');
    let imageFound = bookmarklet.querySelector('.images');
    imageFound.innerHTML = '';
    bookmarklet.style.display = 'block';
    bookmarklet.querySelector('#close')
        .addEventListener('click', function () {
            bookmarklet.style.display = 'none';
        });

    image = document.querySelectorAll('img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"]');
    image.forEach((image) => {
        if (image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {
            const imageFound1 = document.createElement('img');
            imageFound1.src = image.src;
            imageFound.append(imageFound1);
        }
    });

    imageFound.querySelectorAll('img').forEach((image) => {
        image.addEventListener('click', function (ev) {
            imageSelected = ev.target;
            bookmarklet.style.display = 'none';
            window.open(siteUrl +
                `images/create/?url=${encodeURIComponent(imageSelected.src)}&title=${encodeURIComponent(document.title)}`,
                '_blank');
        });
    });
}


bookmarkletLaunch();
