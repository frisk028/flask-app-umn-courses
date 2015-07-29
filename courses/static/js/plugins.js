// place any jQuery/helper plugins in here, instead of separate, slower script files.

(function($) {
    "use strict"
    $.get_attribute = function(attribute_id, family){
    	var cle = { 'HIS':'Historical Perspectives', 'WI': 'Writing Intensive', 
                     'BIOL': 'Biological Sciences', 'PHYS': 'Physical Sciences',
                     'GP': 'Global Perspectives', 'LITR': 'Literature', 'ENV': 'Environment',
                     'DSJ': 'Diversity and Social Justice', 'CIV': 'Civic Life and Ethics',
                     'MATH': 'Mathmatical Thinking', 'AH': 'Arts and Humanities',
                     'TS': 'Technology and Society', 'SOCS': 'Social Sciences'};
        var other = {'TOPICS': 'Topics Course', '08': 'Classroom', 'HON': 'Honors'};
    	if (family == 'CLE') {
    		return cle[attribute_id];
		}
		else {
			return other[attribute_id];
		}
    };
    $.set_attributes = function(attributes, c ) {
        $.each(attributes, function() {
       	  var family = this.family;
       	  var id = this.attribute_id;
       	  var a = $.get_attribute(id, family);
       	  var course_id = '#course_'+c;
		  if (family == 'CLE') {
		  	$(course_id+' > #le').append('<li>'+a+'</li>');
		  	$(course_id+' > #le').addClass('visible');
		  }
		  else  {
		  	$(course_id+' > #other').append('<li>'+a+'</li>');
		  	$(course_id+' > #other').addClass('visible');
		  }
		});
    };
})(jQuery);