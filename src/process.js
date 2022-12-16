let http = require('http');
let formidable = require('formidable');
let fs = require('fs');
const execSync = require('child_process').execSync;


http.createServer(function (req, res) {

  // create an instance of the form object
  let form = new formidable.IncomingForm();

  // create unique temporary directory to store data and results for this session
  let tmp_dir = "./tmp_"
  let random_id = (Math.random() + 1).toString(36).substring(12);
  tmp_dir += random_id + "/";
  if (!fs.existsSync(tmp_dir)) {
    fs.mkdirSync(tmp_dir);
  }

  // process the file upload in Node
  form.parse(req, function (error, fields, file) {
    let filepath = file.fileupload.filepath;
    let newpath = tmp_dir;
    newpath += file.fileupload.originalFilename;

    // copy the uploaded file to a custom folder
    fs.rename(filepath, newpath, function(err) {
      if ( err ) console.log('ERROR: ' + err);
    });

    // process uploaded data
    execSync(
      'source ./venv/bin/activate && livermask --input ' + newpath + ' --output ' + tmp_dir + '/prediction --cpu --verbose',
      { encoding: 'utf-8', stdio: 'inherit' }
    );

    // make it possible for user to download result

    // delete temp dir
    fs.rmSync(tmp_dir, { recursive: true, force: true}, function () {
      // send a NodeJS file upload confirmation message
      res.write('Prediction done!');
      res.end();
    });

  });
}).listen(88);
