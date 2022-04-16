// Javascript Template

// Variables
// qid:string
// usr_choice:list of dict {'choice':None,'correct':False}
// quiz_data:
$(document).ready(function(){
    if (parseInt(qid)==0) {
        console.log('here')
        $("#prev_button").hide();
    }
    if (parseInt(qid)==usr_choice.length-1) {
        console.log('here')
        $("#next_button").text('Submit');
    }
})
