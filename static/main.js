// Javascript Template

$(document).ready(function(){
    $("#positionList").change(function () {
        let positionId = $("#positionList").val();
        window.location.href = "/learn/" + positionId;
        console.log(positionId);
    });
})
