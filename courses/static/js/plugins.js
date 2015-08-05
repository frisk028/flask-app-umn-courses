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
        var other = {'TOPICS': 'Topics Course', '08': 'Classroom', 'HON': 'Honors',
                     '06': 'Independent Study', 'THESIS': 'Thesis Course'};
    	if (family == 'CLE') {
    		return cle[attribute_id]
		}
		else {
      if (other[attribute_id]) {
  			return other[attribute_id]
      }
      else {
        return attribute_id
      }
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
    $.set_day_time = function(meeting_pattern, c, sec) {
      var text = '';
      var start = meeting_pattern[0]['start_time'];
      var end = meeting_pattern[0]['end_time'];
      var time_text = start + "-" + end;
      var course_id = '#course_'+c;
      $.each(meeting_pattern[0]['days'], function() {
        text += this['abbreviation']+" ";
      });
      text = text.trim() + "/" + time_text;
      $(course_id+' > table > #'+sec+' > #dt').append(text);
    }
})(jQuery);