const input = document.getElementById('imageInput');
const img = document.getElementById('profileImg');
const preview = document.getElementById('preview');
const initial = preview.querySelector('.initial');

input.addEventListener('change', function () {
  const file = this.files[0];
  if (file && (file.type === 'image/png' || file.type === 'image/jpeg')) {
    const reader = new FileReader();
    reader.onload = function (e) {
      img.src = e.target.result;
      img.hidden = false;
      initial.style.display = 'none';
    };
    reader.readAsDataURL(file);
  } else {
    alert('Please select a PNG or JPEG image.');
  }
});

const toggleBtn = document.getElementById('toggleBtn');
const dropdownCard = document.getElementById('dropdownCard');

toggleBtn.addEventListener('click', () => {
  dropdownCard.style.display = dropdownCard.style.display === 'block' ? 'none' : 'block';
});

window.addEventListener('click', function (e) {
  if (!toggleBtn.contains(e.target) && !dropdownCard.contains(e.target)) {
    dropdownCard.style.display = 'none';
  }
});