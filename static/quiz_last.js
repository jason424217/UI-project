first = false;
checkMap = {}


function dragChoice(){
    $(".choice").draggable({
        stack: ".choice",
        revert: "invalid"
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
        drop: function (event, ui) {
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
        }
    })
}

function updateMsg(){
    $('#correct-text').text("")
    $('#wrong-text').text("")
    if(Object.keys(checkMap).length != 5){
        return
    }
    for(let key in checkMap){
        if(!checkMap[key]){
            $('#wrong-text').html(`<div><div class="red">Wrong!</div> PG dribbles through back court, stands on top of arc and manage tactic. SG continue running around the half court, as long as he get rid of defender, he can catch ball and shoot outside. SF stand between inside and outside so that he can choose flexible offense and defense transition. PF competes with opponents around paint area and wait for rebound or give a block. C stands under the basket and posts up after obtaining good position.
            <a href="/learn/6" target="_blank">Click here to review again</a>.<div>`)
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
    $('#correct-text').html('<div class="green">Correct!</div>');
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