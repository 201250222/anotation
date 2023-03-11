    function fun1() {
        $.ajax(
            {
                url:"/posttest",
                type:"POST",
                data:{"post1":$("#post1").val()},

                dataType:"json",
                success:function (data) {
                    for ( item in data){
                        console.log(data)
                        var tagName=JSON.stringify(item)
                        $("#lis").append($("<b></b>").text(item+" : "));
                        if(tagName=="法院"){
                            for (court in data[item]){
                                $("#lis").append($("<input type='checkbox' name='userSelect' value='"+court+"' />"));
                                $("#lis").append($("<label></label>").text(court);
                            }
                        }
                        else{
                        $("#lis").append($("<input type='checkbox' name='userSelect' value='"+data[item]+"' />"));
                        $("#lis").append($("<label></label>").text(data[item]));
                        }
                        $("#lis").append($("<br>"));
                    }
                },
                error:function (e) {
                    alert("error");
                }
            }
        )

    }