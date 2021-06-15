frappe.ui.form.on('DocType', {
	refresh: function(frm) {
        frm.trigger('fields_load');

		var pagination = $(frm.wrapper).find('.grid-pagination .btn');
		pagination.each(function() {
			$(this).on("click", function() {
				frm.trigger('fields_load');
			});
		});
    },
    fields_load: function(frm) {
		if (frm.doc.fields) {	
			frm.doc.fields.forEach(function(f, i) {
				cur_frm.cscript.doctype.fields_styles(frm,f);
			});
		}
	}
});

frappe.ui.form.on('DocField', {
	form_render: function(frm,cdn,cdt) {
		frm.trigger('fields_load');
	},
	fieldtype: function(frm,cdn,cdt) {
		frm.trigger('fields_load');
	}
});


cur_frm.cscript.doctype = {
	fields_styles: function(frm,f) {
		var data_row = frm.page.body.find(
			'[data-fieldname="fields"] [data-idx="' + f.idx + '"] .data-row'
		);

		data_row.removeClass("highlight");
		data_row.removeClass("bg-light-1");
		data_row.removeClass("bg-light-2");
		data_row.removeClass("bg-light-3");

		switch(f.fieldtype) {
			case "Section Break":
				data_row.addClass("highlight");
				break;
			case "Column Break":
				data_row.addClass("bg-light-1");
				break;
			default:
				
				break;
		}

	}
}