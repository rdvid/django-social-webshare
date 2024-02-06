(function(){
     if(!window.socialshare) {
         socialshare_js = document.body.appendChild(document.createElement('script'));
         socialshare_js.src = '//mysite.com:8000/static/js/socialshare.js?r='+Math.floor(Math.random()*9999999999999999);
         window.socialshare = true;
     }
     else {
        socialShareLaunch();
     }
})();