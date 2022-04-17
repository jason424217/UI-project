// Javascript Template

// Variables
// qid:string
// usr_choice:list of dict {'choice':None,'correct':False}
// quiz_data:
$(document).ready(function(){
    console.log(usr_choice)
    // Prev and Next button
    if (parseInt(qid)==0) {
        console.log('here')
        $("#prev_button").hide();
    }
    if (parseInt(qid)==usr_choice.length-1) {
        console.log('here')
        $("#next_button").text('Submit');
    }

    // Prefill user choice
    console.log(usr_choice)
    if (usr_choice[parseInt(qid)]['choice']!='None') {
        $("#radios"+usr_choice[parseInt(qid)]['choice']).prop("checked", true);
    }

    // Update user choice
    $('#next_button').click(function() {
        let choice = $('input[name="exampleRadios"]:checked').val();
        if (typeof choice == 'undefined') {
            choice = 'None'
        }
        let correct = 'false';
        if (choice == quiz_data['position']) {
            correct = 'true'
        } else {
            correct = 'false'
        }

        // Ajax call in safari might fail, so make multiple call
        for (let i = 0; i < 5; i++) {
          $.ajax({
                      type: "POST",
                      url: "/update_usr_choice/"+qid,
                      dataType : "json",
                      contentType: "application/json; charset=utf-8",
                      data : JSON.stringify({'choice':choice, 'correct':correct}),
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
        // event.preventDefault();
    });
})
