if (!$) {
    $ = django.jQuery;
}
$(function() {
	$('body').on('click','button[name="status_button"]', function(event) {
		event.preventDefault();
        var mobile_product_id = $(event.target).attr("data-id");
        var data = { id: mobile_product_id, status: 'Offline'};
        $.post( "/update_mobile_product_status/", data,
    		function(response) {
				location.reload();
    	});
	});
});