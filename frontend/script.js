$(document).ready(function () {
    setTimeout(function(){
            $.ajax({url: "https://s3.amazonaws.com/openpose-images/testImage.png", success: function(data, textStatus, request){
                // encode(file.Body)
                //var s = decodeURIComponent(escape(window.atob(result)))
                // console.log(request.getAllResponseHeaders())
                // var uInt8Array = new Uint8Array(data);
                // var i = uInt8Array.length;
                // var binaryString = new Array(i);
                // while (i--)
                // {
                // binaryString[i] = String.fromCharCode(uInt8Array[i]);
                // }
                // var data = binaryString.join('').trim();

                // var base64 = window.btoa(data);

                $("#image").attr('src', `data:image/png;base64,${data}` );
                console.log(data)
                console.log(typeof data)

            }});
    }, 2000);
})

