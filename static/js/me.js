/**
 * Created by baixue on 15-12-9.
 */

function showConfirmModel(taskNum, url) {
    var modal = $('#confirm-modal');
    modal.modal('show');
    modal.find('.modal-body').html("<p>确认要删除<strong>任务"+taskNum+"</strong>吗？");
    modal.find('.modal-footer button').val(url);
}

function taskDel(self) {
    var url = $(self).val();
    $.getJSON(url, function(ret){
        if (ret['msg']=='0'){
            var modal = $('#confirm-modal');
            modal.modal('hide');
            location.reload();
        } else {
            alert(ret['msg']);
        }
    })
}

/*----------------------------------------------------*/
/*	Back To Top Button
/*----------------------------------------------------*/
var pxShow = 300; //height on which the button will show
var fadeInTime = 400; //how slow/fast you want the button to show
var fadeOutTime = 400; //how slow/fast you want the button to hide
var scrollSpeed = 300; //how slow/fast you want the button to scroll to top. can be a value, 'slow', 'normal' or 'fast'

// Show or hide the sticky footer button
jQuery(window).scroll(function() {

    if (jQuery(window).scrollTop() >= pxShow) {
        jQuery("#go-top").fadeIn(fadeInTime);
    } else {
        jQuery("#go-top").fadeOut(fadeOutTime);
    }

});

// Animate the scroll to top
jQuery("#go-top a").click(function() {
    jQuery("html, body").animate({scrollTop:0}, scrollSpeed);
    return false;
});


// 返回上一页并刷新
function backpage(){
    window.location.href=document.referrer;
}

function backtopage(){
    history.go(-1);
    // window.location.reload(true);
    // document.location.reload();
}
