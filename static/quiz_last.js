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
            $('#wrong-text').text("Wrong!")
            return
        }
    }
    $('#correct-text').text("Correct!")
}

$(document).ready(function(){
    dragChoice()
    dropChoice()
})