function generateUI(data){
    $("#position_info").html(data.position)
    $("#position_info").css({"margin-top":"10px","text-decoration":"underline"})
    if(id==6){
        let card=$(`<div>`)
        card.addClass("card")
        let card_body=$(`<div>`)
        card_body.addClass("card-body")
        let img = $(`<div >`).html("")
        img.addClass("col-md-8 text-center")
        img.css({"margin":"10px"})
       
        card_body.html(`<img style="width:100%" src=${data.courtImg}/>`)
        card.append(card_body)
        img.append(card)
        $("#image-row").append(img)
        card_body.append("<b>Court Movement</b>")

        $("#directQuiz").html("Lets take the quiz!");
    }
    else{
    $("#position-img").attr("src",data.courtPosition)
    $("#move-img").attr("src",data.courtMoveMap)
    }
    $("#source").attr("src",data.video)
    
    
    $("#position-text").html(data.description)

    // keep nav bar's seleced option
    $("#positionList").val(id);
}


function fetchData(id){
    $.ajax({
        type:"GET",
        url:"/getdata",
        dataType:"json",
        contentType:"application/json;charset=utf-8",
        data:JSON.stringify({'id':id}),
        success:function(result){
            console.log(result["data"])
            generateUI(result["data"])
            
        },
        error:function(request,status,error){
            console.log("Error")
            console.log(request)
            console.log(status)
            console.log(error)
        }
    })
}

$(document).ready(()=>{
    
    $(".active").removeClass("active");
   $("#study-link").addClass("active");
    fetchData(id)
    console.log(id)
    if(id==1){
        $("#prev").attr('disabled',true)
    }else if(id==6){
        $("#next").attr('disabled',true)
        const row= document.getElementById("image-row")
        while(row.hasChildNodes()){
            row.removeChild(row.firstChild)
        }
    }
    var percentage=(parseInt(id)/6 * 100).toString()
    $(".progress").attr("style","height:30px")
    $(".progress-bar").attr("aria-valuenow",percentage)
    $(".progress-bar").attr("style",`width:${percentage}%`)
    $(".progress-bar").html(`Progress : ${id}/6`)

    $(document).on('click','#prev',()=>{
        
            window.location.href=`/learn/${id-1}`
        
       
    })
    $(document).on('click','#next',()=>{
        
        window.location.href=`/learn/${id+1}`
    
   
    })
    $(document).on('click','.quiz',()=>{

        window.location.href='/'


    })

    $(document).on('click','#directQuiz',()=>{
        window.location.href='/quiz'
    })
    $(document).on('click','.directQuiz',()=>{
        window.location.href='/quiz'
    })
})