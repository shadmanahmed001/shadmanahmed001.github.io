// Get references to the buttons and audio elements
const redButton = document.getElementById('redButton');
const greenButton = document.getElementById('greenButton');
const orangeButton = document.getElementById('orangeButton');

const failedAudio = document.getElementById('failedAudio');
const passedAudio = document.getElementById('passedAudio');
const standAudio = document.getElementById('standAudio');

// Add event listeners to the buttons
redButton.addEventListener('click', () => {
    failedAudio.currentTime = 0.23;
  failedAudio.play(); // Play the "You Failed" audio
});

greenButton.addEventListener('click', () => {
    passedAudio.currentTime = 0.22;
  passedAudio.play(); // Play the "You Passed" audio
});

orangeButton.addEventListener('click', () => {
    standAudio.currentTime = 2.21;
  standAudio.play(); // Play the "Go Stand" audio
});