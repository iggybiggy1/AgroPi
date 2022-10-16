const setCookie = (name, value, expireHours) => {
    var date = new Date();
    date.setTime(date.getTime() + (expireHours * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${date.toUTCString()}`;
}

const getCookie = (name) => {
    var nameString = `${name}=`;
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookies = decodedCookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i];
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(nameString) == 0) {
            return cookie.substring(nameString.length, cookie.length);
        }
    }
    return "";
}
