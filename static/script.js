document.addEventListener("DOMContentLoaded", () => {
    const callBtn = document.getElementById("callBtn");
    const callBtn2 = document.getElementById("callBtn2");
    const callBtn3 = document.getElementById("callBtn3");

    function makeCall() {
        window.location.href = "tel: +260 779 975 968";
    }

    callBtn.addEventListener("click", makeCall);
    callBtn2.addEventListener("click", makeCall);
    callBtn3.addEventListener("click", makeCall);

})

            