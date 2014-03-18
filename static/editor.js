jQuery.download = function (url, data, method) {
	//url and data options required
	if (url && data) {

		//split params into form inputs
		var inputs = '';
		jQuery.each(data, function (key,value) {
			var pair = this;
			inputs += '<input type="hidden" name="' + key + '" value="' + value + '" />';
		});
		//send request
		jQuery('<form enctype="multipart/form-data" action="' + url + '" method="' + (method || 'post') + '">' + inputs + '</form>')
			.appendTo('body').submit().remove();
	}
};

/** A helper method to extract unique values from array (for color palette purposes) **/

Array.prototype.unique = function (a) {
	return function () {
		return this.filter(a)
	}
}(function (a, b, c) {
	return c.indexOf(a, b + 1) < 0
});

 /* CODE EDITOR SETUP */

var editor = ace.edit("editor");
var MapcssMode = require("ace/mode/mapcss").Mode;
editor.getSession().setMode(new MapcssMode());
editor.getSession().on('change', function (e) {
	vm.getHexColors(); //update the color list on style change
});

  /* MAP SETUP */

var map = new L.Map('map', {
	center: new L.LatLng(50.06030, 19.93533), //change hardcoded values to match your area of interest
	zoom: 15
});
var kothic = new L.TileLayer.Kothic('./vtile/{z}/{x}/{y}', {
	minZoom: 3,
	styles: ['fiddle'],
	locales: ['pl'] //change hardcoded language
});
map.addLayer(kothic);


var FiddleVModel = function () {
	var self = this;

	self.icons = ko.observableArray(); //icon library

	self.hexColors = ko.observableArray(); //colors library
    
    /** Extract unique HTML color codes from MapCSS **/
    
	self.getHexColors = function () {
		self.hexColors(editor.getSession().getValue().match(/#[a-z0-9]{6}/gi).unique());
	}
    
    /** Insert icon filename at current cursor position **/
    
	self.insertIcon = function (filename) {
		editor.insert('"icons/' + filename + '"');
		$('#icon-dialog').modal('hide');
	};
    
    /** Insert color code at current cursor position **/
    
	self.insertColor = function (hexcode) {
		editor.insert(hexcode);
	};

    /** Trigger an AJAX submit on upload form, and add icon to library **/
    
	self.uploadIcon = function () {
		$('#icon-load').ajaxForm().ajaxSubmit(function (data) {
			if (data.uploaded) {
				self.icons.push(data.uploaded); //no need to refresh the whole list, just add new entry to icons array
			} else {
				alert('Upload error');
			}
		});
	};

    /** Read the icon library contents from server **/

	self.getIcons = function () {
		$.getJSON('./icons', function (data) {
			self.icons(data.icons);
		});
	}

   /** Post the MapCSS to compiler and eval the result **/

	self.renderStyle = function () {

		$.post('./compile', {
				"name": "fiddle",
				"css": editor.getSession().getValue() //get the editor contents
			},
			function (data) {
				eval(data); //Yes, I have been warned that using eval() causes the ozone hole to grow, and Firefox to crash. 
				try {
					kothic.enableStyle('converted'); //try to apply the evaluated style to Kothic and redraw
					kothic.redraw();
				} catch (e) {
					alert('The style provided cannot be used');
				}

			});

	};

    /** PRIVATE: download the style from server in desired format **/

	self._download = function (format) {
		$.download(
			'./download', {
				"name": "fiddle",
				"css": editor.getSession().getValue(),
				"format": format
			},
			'POST'
		)
	}

   /** Download the style in compiled JS format **/

	self.downloadJs = function () {
		return self._download('js')
	}

   /** Download the style in unchanged MapCSS format **/

	self.downloadCss = function () {
		return self._download('css');
	}
	
	/** Show the color picker, and insert the resulting hex code on pick **/

	self.pickAColor = function () {
		$.jeegoocolor({
			draggable: true,
			top: 50,
			left: 50,
			overlay: false,
			onPick: function (hexcolor) {
				editor.insert("#" + hexcolor);
			}
		});
	}
   
   /** Show the icon library dialog **/
   
	self.pickAnIcon = function () {
		$('#icon-dialog').modal('show');
	};

    //Get the initial icon list (from server) and color list (from MapCSS)
    
	self.getIcons();
	self.getHexColors();
}


var vm = new FiddleVModel();
ko.applyBindings(vm);
