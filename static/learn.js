function generateUI(data){
    if(id==6){
        // let row=document.getElementById("image-row")
        let img = $(`<div >`).html(`<img style="width:100%" src=${data.courtImg}/>`)
        img.addClass("col-md-8 text-center")
        img.css({"margin":"10px"})
        $("#image-row").append(img)
        img.append("Court Movement")

        let button = $("<button>").html(`<a href="/quiz">Wanna take the quiz now?</a>`)
        button.addClass("btn btn-warning quiz")
        button.css("color","white")
        $("#quiz-button").append(button)
    }
    else{
    $("#position-img").attr("src",data.courtPosition)
    $("#move-img").attr("src",data.courtMoveMap)
    }
    $("#source").attr("src",data.video)
    
    
    $("#position-text").html(data.description)

}


function fetchData(id){
    $.ajax({
        type:"GET",
        url:"/getdata",
        dataType:"json",
        contentType:"application/json;charset=utf-8",
        data:JSON.stringify({'id':id}),
        success:function(result){
            console.log(result.data)
            generateUI(result.data)
            
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
        
    window.location.href=`/`


})

})