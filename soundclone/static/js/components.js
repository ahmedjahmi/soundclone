$(document).ready(function() {
	$('.modal--trigger').on('click', function() {
		$('.modal--overlay').addClass('active');
	})
	$('.modal--close').on('click', function() {
		$('.modal--overlay').removeClass('active');
	})
	$('.modal--overlay').on('click', function(event) {
		var modalHasClass = $(event.target).hasClass('modal--overlay active')
		if (modalHasClass) {
			$('.modal--overlay').removeClass('active');
		}
	})
	$(document).on('keydown', function(event) {
		if (event.key === 'Escape') {
			$('.modal--overlay').removeClass('active');
		}
	})
})
