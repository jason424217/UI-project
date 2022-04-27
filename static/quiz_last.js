first = false;
checkMap = {}

function dragChoice(){
    $(".choice").draggable({
        scroll: false,
        stack: ".choice",
        revert: "invalid",
    })
}

function stringValid(a) {
    aStr = String(a)
    if(aStr && aStr.length > 0){
        return true
    }
    return false
}

function dropChoice() {
    $('.pos').droppable({
        accept: ".choice",
        drop: function (event, ui) {
            var $this = $(this);
            let choice = $(ui.draggable).data('choice')
            let pos = $(this).data('pos')
            console.log("choice and pos are " + choice + " and " + pos);
            if(stringValid(pos) && stringValid(choice) && String(choice) === String(pos)){
                checkMap[pos] = true
            }else{
                checkMap[pos] = false
            }
            first = true;
            updateMsg()
            ui.draggable.position({
                my: "center",
                at: "center",
                of: $this,
                using: function(pos) {
                  $(this).animate(pos, "slow", "linear");
                }
              });
        }
    })
}

function updateMsg(){
    $('#hint-text').text("")
    $('#hint-text').addClass("display-none");
    if(Object.keys(checkMap).length != 5){
        return
    }
    for(let key in checkMap){
        if(!checkMap[key]){
            $('#hint-text').html(`<div class="darkgrey"><div class="red">Wrong!</div> PG dribbles through back court. SG continue running around the half court. SF stand between inside and outside PF competes with opponents around paint area. C stands under the basket.
            <a href="/learn/6" target="_blank">Click here to review again</a>.<div>`)
            $('#hint-text').removeClass("display-none");
            $.ajax({
                type: "POST",
                url: "/update_usr_choice/"+qid,                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify({'choice':checkMap, 'correct':'False'}),
                success: function(result){
                    console.log("success")
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
            return
        }
    }
    $('#hint-text').html('<div class="green">Correct!</div>');
    $('#hint-text').removeClass("display-none");
    $.ajax({
        type: "POST",
        url: "/update_usr_choice/"+qid,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify({'choice':checkMap, 'correct':'True'}),
        success: function(result){
            console.log("success")
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

$(document).ready(function(){
    dragChoice()
    dropChoice()
})