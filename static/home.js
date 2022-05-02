$(document).ready(()=>{
    // $(document).on('click','#lea',()=>{
    //     console.log("learn button");
    //     window.location.href="/learn/1"
    // });
    //
    // $(document).on('click',"#quiz-button",()=>{
    //     console.log("quiz button");
    //     window.location.href="/quiz"
    // });

    $("#learn-button").click(function () {
        window.location.href="/learn/1"
    });

    $("#quiz-button").click(function () {
        window.location.href="/quiz"
    });
})