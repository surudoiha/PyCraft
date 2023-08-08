const numInput = document.querySelector('input[type="number"]');

numInput.addEventListener('input', function() {
  this.value = this.value.replace(/[e\+\-]/gi, ' ');
});