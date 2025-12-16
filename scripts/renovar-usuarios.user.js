// ==UserScript==
// @name     Script sin nombre 336214
// @version  1
// @grant    none
// @match    https://www-pre.gobiernodecanarias.org/selfservice-ext/pub/changeAccountsPassword*
// ==/UserScript==


function enableClipboard() {
   unsafeWindow.console.log("Habilitando portapapeles");
   var _handler = function(event) {
   	  event.stopImmediatePropagation();
      return true;
      }
	 document.addEventListener('copy', _handler, true);
	 document.addEventListener('paste', _handler, true);
	 document.addEventListener('onpaste', _handler, true);
   unsafeWindow.console.log("OK");
   }


function enableFields(_evt) {
   unsafeWindow.console.log("Habilitando campos de texto/password");
   const password =  prompt("Nueva constraseña: ", "renovación usuarios delegados");
   unsafeWindow.console.log("password:", password);
  
   var newPassword = document.getElementById('newPassword');
   if (newPassword) {
      unsafeWindow.console.log("newPAssword:", newPassword);
      newPassword.type = 'text';
      newPassword.value = password;
      }

   var newPasswordConfirm = document.getElementById('newPasswordConfirm');
   if (newPasswordConfirm) {
      unsafeWindow.console.log("newPasswordConfirm:", newPasswordConfirm);
      newPasswordConfirm.type = 'text'; 
      newPasswordConfirm.value = password
      }
   unsafeWindow.console.log("OK");
   }


function onPageFullyLoaded() {
	 enableClipboard();
   setTimeout(enableFields, 1000);
   }


window.addEventListener ("load", onPageFullyLoaded);