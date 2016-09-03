/* jQuery Plugin ScrollAdvance v1.0.0 | (c) 2014 totodunet, (http://totodu.net/) | Licensed under the MIT License (http://opensource.org/licenses/MIT) | Requires: jQuery 1.6.0+ */
(function(e){e.fn.scrollBottom=function(t,n){if(t==null){if(e(this).is(document))return e(this).height()-e(this).scrollTop()-e(window).height();else return e(this).prop("scrollHeight")-e(this).prop("offsetHeight")-e(this).scrollTop()}else{if(n==null||!e.isPlainObject(n)){if(e(this).is(document))e("html, body").scrollTop(e(this).height()-e(window).height()-t);else e(this).scrollTop(e(this).prop("scrollHeight")-e(this).prop("offsetHeight")-t)}else{if(e(this).is(document))e("html, body").animate({scrollTop:e(this).height()-e(window).height()-t},n);else e(this).animate({scrollTop:e(this).prop("scrollHeight")-e(this).prop("offsetHeight")-t},n)}}return this};e.fn.scrollRight=function(t,n){if(t==null){if(e(this).is(document))return e(this).width()-e(this).scrollLeft()-e(window).width();else return e(this).prop("scrollWidth")-e(this).prop("offsetWidth")-e(this).scrollLeft()}else{if(n==null||!e.isPlainObject(n)){if(e(this).is(document))e("html, body").scrollLeft(e(this).width()-e(window).width()-t);else e(this).scrollLeft(e(this).prop("scrollWidth")-e(this).prop("offsetWidth")-t)}else{if(e(this).is(document))e("html, body").animate({scrollLeft:e(this).width()-e(window).width()-t},n);else e(this).animate({scrollLeft:e(this).prop("scrollWidth")-e(this).prop("offsetWidth")-t},n)}}return this};e.fn.scrollCenter=function(t,n,r){if(t==null){if(e(this).is(document))return{x:Math.round(e(this).scrollLeft()+e(window).width()/2),y:Math.round(e(this).scrollTop()+e(window).height()/2)};else return{x:Math.round(e(this).scrollLeft()+e(this).prop("offsetWidth")/2),y:Math.round(e(this).scrollTop()+e(this).prop("offsetHeight")/2)}}else if(t!=parseInt(t)&&t!=parseFloat(t)){if(n==null||!e.isPlainObject(n))return e(this).scrollCenter(t.position().left+t.width()/2,t.position().top+t.height()/2);else if(e.isPlainObject(n))e(this).scrollCenter(t.position().left+t.width()/2,t.position().top+t.height()/2,n)}else{if(r==null||!e.isPlainObject(r)){if(e(this).is(document)){e("html, body").scrollLeft(t-Math.round(e(window).width()/2));e("html, body").scrollTop(n-Math.round(e(window).height()/2))}else{e(this).scrollLeft(t-Math.round(e(this).prop("offsetWidth")/2));e(this).scrollTop(n-Math.round(e(this).prop("offsetHeight")/2))}}else{if(e(this).is(document))e("html, body").animate({scrollLeft:t-Math.round(e(window).width()/2),scrollTop:n-Math.round(e(window).height()/2)},r);else e(this).animate({scrollLeft:t-Math.round(e(this).prop("offsetWidth")/2),scrollTop:n-Math.round(e(this).prop("offsetHeight")/2)},r)}}return this};e.fn.scrollTopRight=function(t,n){if(n==null||!e.isPlainObject(n)){if(e(this).is(document)){e(this).scrollRight(e(this).width()-t.position().left-t.width());e("html, body").scrollTop(t.position().top)}else{e(this).scrollRight(e(this).width()-t.position().left-t.width());e(this).scrollTop(t.position().top)}}else{if(e(this).is(document))e("html, body").animate({scrollLeft:e(this).width()-e(window).width()-e(this).width()+t.position().left+t.width(),scrollTop:t.position().top},n);else e(this).animate({scrollLeft:e(this).prop("scrollWidth")-e(this).prop("offsetWidth")-e(this).width()+t.position().left+t.width(),scrollTop:t.position().top},n)}return this};e.fn.scrollTopLeft=function(t,n){if(n==null||!e.isPlainObject(n)){if(e(this).is(document)){e("html, body").scrollLeft(t.position().left);e("html, body").scrollTop(t.position().top)}else{e(this).scrollLeft(t.position().left);e(this).scrollTop(t.position().top)}}else{if(e(this).is(document))e("html, body").animate({scrollLeft:t.position().left,scrollTop:t.position().top},n);else e(this).animate({scrollLeft:t.position().left,scrollTop:t.position().top},n)}return this};e.fn.scrollBottomLeft=function(t,n){if(n==null||!e.isPlainObject(n)){if(e(this).is(document))e("html, body").scrollLeft(t.position().left);else e(this).scrollLeft(t.position().left);e(this).scrollBottom(e(this).height()-t.position().top-t.height())}else{if(e(this).is(document))e("html, body").animate({scrollLeft:t.position().left,scrollTop:e(this).height()-e(window).height()-e(this).height()+t.position().top+t.height()},n);else e(this).animate({scrollLeft:t.position().left,scrollTop:e(this).prop("scrollHeight")-e(this).prop("offsetHeight")-e(this).height()+t.position().top+t.height()},n)}return this};e.fn.scrollBottomRight=function(t,n){if(n==null||!e.isPlainObject(n)){e(this).scrollRight(e(this).width()-t.position().left-t.width());e(this).scrollBottom(e(this).height()-t.position().top-t.height())}else{if(e(this).is(document))e("html, body").animate({scrollLeft:e(this).width()-e(window).width()-e(this).width()+t.position().left+t.width(),scrollTop:e(this).height()-e(window).height()-e(this).height()+t.position().top+t.height()},n);else e(this).animate({scrollLeft:e(this).prop("scrollWidth")-e(this).prop("offsetWidth")-e(this).width()+t.position().left+t.width(),scrollTop:e(this).prop("scrollHeight")-e(this).prop("offsetHeight")-e(this).height()+t.position().top+t.height()},n)}return this}})(jQuery)