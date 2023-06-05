const redHeader = $('#red_header');
const header = $('header');
redHeader.on('click', changeColor);

function changeColor () {
  header.css('color', '#FF0000');
}
