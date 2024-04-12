import '../css/main.css';
import './alpine.config.js';
import './htmx.config.js';

function component() {
  const element = document.createElement('div');
  element.innerHTML = 'Hello webpack';
  return element;
}

document.addEventListener('DOMContentLoaded', () => {
  document.body.appendChild(component());
});