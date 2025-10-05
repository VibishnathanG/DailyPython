from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Pomodoro Timer</title>
    <style>
        body {
            background-color: #f7f5dd;
            font-family: 'Courier New', monospace;
            text-align: center;
            padding: 50px;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
        .session-type {
            font-size: 36px;
            margin: 20px 0;
            color: #0a8a27;
        }
        .buttons {
            margin: 30px 0;
        }
        button {
            font-size: 18px;
            padding: 15px 30px;
            margin: 0 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #9bdeac;
        }
        button:hover {
            background-color: #7bc97b;
        }
        .progress {
            font-size: 24px;
            margin: 20px 0;
            color: #e7305b;
        }
        .tomato {
            width: 200px;
            height: 200px;
            background-color: #e7305b;
            border-radius: 50%;
            margin: 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="session-type" id="sessionType">Timer</h1>
        <div class="tomato">
            <span id="timerDisplay">00:00</span>
        </div>
        <div class="buttons">
            <button onclick="startTimer()">START</button>
            <button onclick="resetTimer()">RESET</button>
        </div>
        <div class="progress" id="progress"></div>
    </div>

    <script>
        let reps = 0;
        let timer = null;
        let isRunning = false;
        
        const WORK_MIN = 2;
        const SHORT_BREAK_MIN = 1;
        const LONG_BREAK_MIN = 2;

        function formatTime(seconds) {
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
        }

        function updateProgress() {
            const workSessions = Math.floor(reps / 2);
            document.getElementById('progress').textContent = '✓'.repeat(workSessions);
        }

        function countDown(count, sessionType) {
            document.getElementById('timerDisplay').textContent = formatTime(count);
            document.getElementById('sessionType').textContent = sessionType;
            
            if (count > 0 && isRunning) {
                timer = setTimeout(() => countDown(count - 1, sessionType), 1000);
            } else if (isRunning) {
                startTimer();
                updateProgress();
            }
        }

        function startTimer() {
            if (!isRunning) {
                isRunning = true;
            }
            
            reps++;
            
            const workSec = WORK_MIN * 60;
            const shortBreakSec = SHORT_BREAK_MIN * 60;
            const longBreakSec = LONG_BREAK_MIN * 60;
            
            if (reps % 8 === 0) {
                countDown(longBreakSec, 'Long Break');
            } else if (reps % 2 === 0) {
                countDown(shortBreakSec, 'Break');
            } else {
                countDown(workSec, 'Work');
            }
        }

        function resetTimer() {
            isRunning = false;
            if (timer) {
                clearTimeout(timer);
            }
            reps = 0;
            document.getElementById('timerDisplay').textContent = '00:00';
            document.getElementById('sessionType').textContent = 'Timer';
            document.getElementById('progress').textContent = '';
        }
    </script>
</body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)