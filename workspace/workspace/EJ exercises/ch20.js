var http = require("http");
var fs = require("fs");

// EXERCISE 1

var types = ['text/plain', 'text/html', 'application/json'];
var getData = function(host, path, headers) {
    for (var i = 0; i < headers.length; i++) {
        var request = http.request({
            hostname: host,
            path: path,
            method: "GET",
            headers: {
                Accept: headers[i]
            }
        }, function(response) {
            try {
                read(response, done);
            } catch(e) {
                console.log('error');
            }
        });
        request.end();
    }
}

var done = function(error, data) {
    if (error) {
        //(error);
    } else {
        console.log(data);
    }
};

var read = function(stream, done) {
    var data = "";
    stream.on("data", function(chunk) {
        data += chunk.toString();
    });
    stream.on("end", function() {
        done(null, data);
    });
    stream.on("error", function(error) {
        done(error, data);
    });
};

getData("eloquentjavascript.net", "/", types);






/*
function urlToPath(url) {
  var path = require("url").parse(url).pathname;
  
  var cut = 0;
  for(var i = 0; i < path.length; i++) {
      var index = path.indexOf('..', i);
      if(index > -1) {
          cut = index + 2;
      }
  }
  path = path.slice(cut, path.length);
  return "." + decodeURIComponent(path);
}

console.log(urlToPath('http://myhostname:8000/../../../etc/passwd'));



*/



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

