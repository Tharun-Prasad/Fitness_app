// script.js

document.querySelectorAll('.card').forEach(card => {
    let timer;
    let isRunning = false;
    let [milliseconds, seconds, minutes] = [0, 0, 0];
    
    const display = card.querySelector('.display');
    const startStopButton = card.querySelector('.startStop');
    const resetButton = card.querySelector('.reset');
    
    function updateDisplay() {
        let m = minutes < 10 ? `0${minutes}` : minutes;
        let s = seconds < 10 ? `0${seconds}` : seconds;
        let ms = milliseconds < 10 ? `0${milliseconds}` : milliseconds;
    
        display.innerText = `${m}:${s}:${ms}`;
    }
    
    function startStopwatch() {
        timer = setInterval(() => {
            milliseconds++;
            if (milliseconds == 100) {
                milliseconds = 0;
                seconds++;
            }
            if (seconds == 60) {
                seconds = 0;
                minutes++;
            }
            updateDisplay();
        }, 10);
    }
    
    function stopStopwatch() {
        clearInterval(timer);
    }
    
    startStopButton.addEventListener('click', () => {
        if (isRunning) {
            stopStopwatch();
            startStopButton.textContent = 'Start';
        } else {
            startStopwatch();
            startStopButton.textContent = 'Stop';
        }
        isRunning = !isRunning;
    });
    
    resetButton.addEventListener('click', () => {
        stopStopwatch();
        [milliseconds, seconds, minutes] = [0, 0, 0];
        updateDisplay();
        startStopButton.textContent = 'Start';
        isRunning = false;
    });
    });