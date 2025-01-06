let mediaRecorder;
let audioChunks = [];

const startButton = document.getElementById('start-btn');
const stopButton = document.getElementById('stop-btn');
const transcriptionField = document.getElementById('transcription');

// Запрос доступа к микрофону и настройка MediaRecorder
startButton.addEventListener('click', async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
    };

    mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        audioChunks = [];
        sendAudioToServer(audioBlob);
    };

    mediaRecorder.start();
    startButton.disabled = true;
    stopButton.disabled = false;
    setTimeout(stopRecords, 15000);
});


//stopButton.addEventListener('click', () => {
//    mediaRecorder.stop();
//    startButton.disabled = false;
//    stopButton.disabled = true;
//});

const stopRecords = () => {
    mediaRecorder.stop();
    startButton.disabled = false;
    stopButton.disabled = true;
};

async function sendAudioToServer(audioBlob) {
    const formData = new FormData();
    formData.append('audio', audioBlob);
    console.log(formData);

    try {
        const response = await fetch('http://127.0.0.1:5050/server', {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            transcriptionField.textContent = result.transcription || 'Нет текста';
        } else {
            transcriptionField.textContent = 'Ошибка распознавания';
        }
    } catch (error) {
        console.error('Ошибка при отправке аудио:', error);
        transcriptionField.textContent = 'Ошибка при соединении с сервером';
    }
}