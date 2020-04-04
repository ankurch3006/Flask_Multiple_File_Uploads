$(function(){

    var fileUploadFail = function(data){};


    var dragHandler = function(evt){
        evt.preventDefault();
    };

    var dropHandler = function(evt){debugger;
        evt.preventDefault();
        var files = evt.originalEvent.dataTransfer.files;

        var formData = new FormData();
        for(i=0; i<files.length; i++) {
            formData.append("file", files[i]);
        }
        var req = {
            url: "/",
            method: "post",
            processData: false,
            contentType: false,
            data: formData,
            success: function (data) {
                   alert("Uploaded Succesfully!");
            }
        };

        var promise = $.ajax(req);
        promise.then(fileUploadSuccess, fileUploadFail);
    };

    var dropHandlerSet = {
        dragover: dragHandler,
        drop: dropHandler
    };

    $(".droparea").on(dropHandlerSet);

    fileUploadSuccess(false); // called to ensure that we have initial data
});