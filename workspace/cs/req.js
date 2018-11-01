function urlToPath(url) {
  var path = require("url").parse(url).pathname;
  /*
  var cut = 0;
  for(var i = 0; i < path.length; i++) {
      var index = path.indexOf('..', i);
      if(index > -1) {
          cut = index + 2;
      }
  }
  path = path.slice(cut, path.length);*/
  return "." + decodeURIComponent(path);
}

console.log(urlToPath('http://myhostname:8000/../../../etc/passwd'));
var fs = require("fs");
var methods = Object.create(null);

methods.MKCOL = function(path, respond) {
    fs.stat(path, function(error, stats) {
        if (error && error.code == "ENOENT") {
            fs.mkdir(path, resp(respond));
        }
        else if (error) {
            respond(500, error.toString());
        }
        else if (stats.isDirectory()) {
            respond(204);
        }
        else {
            respond(400, "File exists");
        }
    });
};

var resp = function(respond) {
    return function(error) {
        if (error)
            respond(500, error.toString());
        else
            respond(204);
    };
}

