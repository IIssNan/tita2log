/*
Copyright (c) 2003-2010, CKSource - Frederico Knabben. All rights reserved.
For licensing, see LICENSE.html or http://ckeditor.com/license
*/

CKEDITOR.editorConfig = function( config )
{
	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
	
	config.toolbar = 'Qzone';
	
	    config.toolbar_Qzone =
	    [
	        ['Font','FontSize'],
	        ['Bold','Italic','Underline','Strike'],
	        ['TextColor','BGColor','-','Outdent','Indent','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','-','Maximize'],
	        '/',
	        ['Smiley','Image','Vedio','Flash','-','NumberedList','BulletedList','Blockquote'],
	        ['Undo','Redo']
	    ];
};
