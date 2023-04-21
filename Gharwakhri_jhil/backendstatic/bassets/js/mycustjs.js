
// 
const toggle = document.getElementById('dark-mode-toggle');
const body = document.body;
const isDarkMode = localStorage.getItem('dark-mode') === 'true';

if (isDarkMode) {
  body.classList.add('dark', 'dark-mode');
}

toggle.addEventListener('click', () => {
  const isDarkMode = body.classList.toggle('dark-mode');
  localStorage.setItem('dark-mode', isDarkMode);
});



