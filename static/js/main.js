(function($) {

	"use strict";


})(jQuery);

($(document).ready(function() {
alertResMsg(gTxt("${resMap.msg}"));

$("#resv_age10").on("propertychange change paste input", function() {

    var resv_age10 = fnReplace($("#resv_age10").val());
    var resv_age20 = fnReplace($("#resv_age20").val());
    var resv_age30 = fnReplace($("#resv_age30").val());
    var resv_age40 = fnReplace($("#resv_age40").val());
    var resv_age50 = fnReplace($("#resv_age50").val());

    $("#resv_number").val(resv_age10 + resv_age20 + resv_age30 + resv_age40 + resv_age50);
});

$("#resv_age20").on("propertychange change paste input", function() {

    var resv_age10 = fnReplace($("#resv_age10").val());
    var resv_age20 = fnReplace($("#resv_age20").val());
    var resv_age30 = fnReplace($("#resv_age30").val());
    var resv_age40 = fnReplace($("#resv_age40").val());
    var resv_age50 = fnReplace($("#resv_age50").val());

    $("#resv_number").val(resv_age10 + resv_age20 + resv_age30 + resv_age40 + resv_age50 );
});

$("#resv_age30").on("propertychange change paste input", function() {

    var resv_age10 = fnReplace($("#resv_age10").val());
    var resv_age20 = fnReplace($("#resv_age20").val());
    var resv_age30 = fnReplace($("#resv_age30").val());
    var resv_age40 = fnReplace($("#resv_age40").val());
    var resv_age50 = fnReplace($("#resv_age50").val());

    $("#resv_number").val(resv_age10 + resv_age20 + resv_age30 + resv_age40 + resv_age50 );
});

$("#resv_age40").on("propertychange change paste input", function() {

    var resv_age10 = fnReplace($("#resv_age10").val());
    var resv_age20 = fnReplace($("#resv_age20").val());
    var resv_age30 = fnReplace($("#resv_age30").val());
    var resv_age40 = fnReplace($("#resv_age40").val());
    var resv_age50 = fnReplace($("#resv_age50").val());

    $("#resv_number").val(resv_age10 + resv_age20 + resv_age30 + resv_age40 + resv_age50 );
});

$("#resv_age50").on("propertychange change paste input", function() {

    var resv_age10 = fnReplace($("#resv_age10").val());
    var resv_age20 = fnReplace($("#resv_age20").val());
    var resv_age30 = fnReplace($("#resv_age30").val());
    var resv_age40 = fnReplace($("#resv_age40").val());
    var resv_age50 = fnReplace($("#resv_age50").val());

    $("#resv_number").val(resv_age10 + resv_age20 + resv_age30 + resv_age40 + resv_age50 );
});

});


function fnReplace(val) {
    var ret = 0;
    if(typeof val != "undefined" && val != null && val != ""){
        ret = Number(val.replace(/,/gi,''));
    }
    return ret;
})(jQuery);
