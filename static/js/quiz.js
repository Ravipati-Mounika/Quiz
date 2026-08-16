let timeLeft = 300;

const timerElement = document.getElementById("timer");
const quizForm = document.getElementById("quizForm");

if (timerElement && quizForm) {

    const timer = setInterval(function () {

        let minutes = Math.floor(timeLeft / 60);
        let seconds = timeLeft % 60;

        seconds = seconds < 10
            ? "0" + seconds
            : seconds;

        timerElement.textContent =
            minutes + ":" + seconds;

        timeLeft--;

        if (timeLeft < 0) {

            clearInterval(timer);

            alert(
                "Time is up! Your quiz will be submitted."
            );

            quizForm.submit();
        }

    }, 1000);
}