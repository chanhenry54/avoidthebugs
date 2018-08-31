var prov = new firebase.auth.GithubAuthProvider();
var auth = firebase.auth();

$('#g_login').click(function() {
    auth.signInWithPopup(prov).then(function(result) {
        var tok = result.credential.accessToken;
        var user = result.user;

        console.log(JSON.stringify(user));
        var uid = user.uid;
        var name = user.providerData[0].displayName;
        if (name == null) { name = user.providerData[0].uid; }

        $.cookie('uid', uid);
        $.cookie('dname', name);
        $.cookie('edate', user.stsTokenManager.expirationTime);

        $('#auth').hide();
        $('#gameplay').show();
    }).catch(function(error) {
        var errorCode = error.code;
        var errorMsg = error.message;

        console.log(errorCode + ': ' + errorMsg);
    });
});

function loggedIn() {
    var expir = $.cookie('edate');
    if (expir == null) {
        return false;
    } else {
        var current = Date.now();
        return not ((current - expir) > 0);
    }
}

if (loggedIn()) {
    // session good i guess.
    $('#auth').hide();
    $('#gameplay').show();
}