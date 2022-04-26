// Javascript Template

// Variables
// qid:string
// usr_choice:list of dict {'choice':None,'correct':False}
// quiz_data:
$(document).ready(function(){
    // Render card border
    // "box-shadow: blue 0px 0px 0px 2px inset," ";"
//    let card_border = ["blue 0px 0px 0px 2px", "rgb(255, 255, 255) 10px -10px 0px -3px", "rgb(31, 193, 27) 10px -10px", "rgb(255, 255, 255) 20px -20px 0px -3px", "rgb(255, 217, 19) 20px -20px", "rgb(255, 255, 255) 30px -30px 0px -3px", "rgb(255, 156, 85) 30px -30px", "rgb(255, 255, 255) 40px -40px 0px -3px", "rgb(255, 85, 85) 40px -40px"]
//
//    let border_idx = 2*parseInt(qid)
//    console.log(border_idx)
//    let card_border_css = card_border[border_idx]+' inset, '+card_border.slice(border_idx+1).join(', ')
//    console.log(card_border_css);
//    $('.quiz-mcq').css("box-shadow", card_border_css);

    console.log(usr_choice);
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
        let choice_ele = $('.quiz-options[value='+usr_choice[parseInt(qid)]['choice']+']')
        let choice = choice_ele.attr('value')
        choice_ele.css('background-color','rgb(173,216,230)')
        if (quiz_data['position'] === choice) {
            choice_ele.find('.correct-svg').removeClass("display-none");
        } else {
            choice_ele.find('.wrong-svg').removeClass("display-none");
            $('.quiz-options[value='+quiz_data['position']+']').find('.correct-svg').removeClass("display-none");
            $('.quiz-explain').removeClass("display-none");
        }
    }

    // Update user choice
    $('.quiz-options').click(function() {
        if (usr_choice[parseInt(qid)]['choice']!='None') {
            return
        }
        let choice = $(this).attr('value')

        // Show ans and explain
        $(this).css('background-color','rgb(173,216,230)')
        if (quiz_data['position'] === choice) {
            $(this).find('.correct-svg').removeClass("display-none");
        } else {
            $(this).find('.wrong-svg').removeClass("display-none");
            $('.quiz-options[value='+quiz_data['position']+']').find('.correct-svg').removeClass("display-none");
            $('.quiz-explain').removeClass("display-none");
        }

        //
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
                          usr_choice = result.data
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
