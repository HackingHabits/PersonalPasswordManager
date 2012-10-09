decrypt_password = function(encrypted_data, item_id){	
	var master_password = $("#masterPassword").val();
	
	/* Validations */
	if (master_password == "") {
		alert("Your master password is needed for all operations");
		return;
	}	
	try{
		password = sjcl.decrypt(master_password, encrypted_data);
		$(".secret_password").html("");
		$("#decrypt_password_"+item_id).html(password);
	}catch(err){
		alert("Your master password must be wrong");
	};
};

toggle_keyboard = function(){
	$("#keyboard_container").toggle();
};

encrypt_new_password = function(obj){
	var master_password = $("#masterPassword").val();
	var website         = $("#inputWebsite").val();
	var password        = $("#inputPassword").val();
	var decrypted_password = "";
	
	/* Validations */
	if (master_password == "") {
		alert("Your master password is needed for all operations");
		return;
	}

	if (website == "") {
		alert("Your website name cannot be empty");
		return;
	}
	
	if (password == "") {
		alert("Your password cannot be empty");
		return;
	}
	
	encrypted_data = sjcl.encrypt(master_password, password);	
	$.post('/',{website:website,password:encrypted_data}, function(data){
		location.reload();
	});	
};

$(document).ready(function(){
	$(".container input").focus(function(){
		set_focus($(this));		
	});
});