// Copy the Generated Subtitle JSON List from the Python Code. The sample JSON List is attached for reference below
const subtitles = [
  { "start_time": 1, "end_time": 5, "translated_text": "Hello, welcome to the Github Project by Anubhav9" },
  { "start_time": 6, "end_time": 10, "translated_text": "We're currently translating the subtitles" }
];

const subtitleStyle = `
  position: absolute;
  top: 30%;
  width: 100%;
  text-align: center;
  font-size: 22px;
  font-weight: bold;
  color: red;
  background-color: white;
  padding: 5px;
  border-radius: 5px;
  z-index: 9999;
`;

function showSubtitle(text) {
  let subtitleDiv = document.querySelector('#custom-subtitle');
  if (!subtitleDiv) {
    subtitleDiv = document.createElement('div');
    subtitleDiv.id = 'custom-subtitle';
    subtitleDiv.style = subtitleStyle;
    document.body.appendChild(subtitleDiv);
  }
  subtitleDiv.innerText = text;
}

function clearSubtitle() {
  const subtitleDiv = document.querySelector('#custom-subtitle');
  if (subtitleDiv) subtitleDiv.innerText = '';
}

function playSubtitles() {
  subtitles.forEach((subtitle) => {
    setTimeout(() => showSubtitle(subtitle.translated_text), subtitle.start_time * 1000);
    setTimeout(clearSubtitle, subtitle.end_time * 1000);
  });
}

playSubtitles();
