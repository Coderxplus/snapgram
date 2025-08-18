const dropdown = document.querySelector('.dropdown');
const menu = document.querySelector('.dropdown-menu');
const fileInput = document.getElementById("profile_pic");
const preview = document.getElementById("preview-pic");


dropdown.addEventListener('click', () => {
  menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
});

document.addEventListener('click', (e) => {
  if (!dropdown.contains(e.target)) {
    menu.style.display = 'none';
  }
});


  

fileInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    if (file) {
      preview.src = URL.createObjectURL(file); // Change image preview
    }
});

