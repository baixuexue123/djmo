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