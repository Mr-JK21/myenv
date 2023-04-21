function previewImage(event) {
    var image = document.getElementById('imagePreview');
    image.style.display = 'block';
    image.src = URL.createObjectURL(event.target.files[0]);
  }