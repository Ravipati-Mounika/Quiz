let time = 5 * 60;

const timer = document.getElementById("timer");

const quizForm = document.getElementById("quizForm");

const countdown = setInterval(function () {

    let minutes = Math.floor(time / 60);
    let seconds = time % 60;

    seconds = seconds < 10
        ? "0" + seconds
        : seconds;

    timer.innerHTML =
        minutes + ":" + seconds;

    if (time <= 0) {

        clearInterval(countdown);

        alert("Time is over!");

        quizForm.submit();
    }

    time--;

}, 1000);