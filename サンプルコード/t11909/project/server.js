const path = require('path');
const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');

const API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxx';

const server = express();

server.use(bodyParser.json({limit: '10mb'}));
server.use(express.static(path.join(__dirname, 'public')));

server.post('/gvision', (req, res) => {
  const options = {
    uri: 'https://vision.googleapis.com/v1/images:annotate?key=' + API_KEY,
    headers: {
      'Content-type': 'application/json',
    },
    json: req.body
  }
  request.post(options, (error, response, body) => {
    if (response.statusCode === 200) {
      res.header('Content-Type', 'application/json; charset=utf-8');
      res.send(body);
    } else {
      res.status(response.statusCode);
      res.send({});
    }
  });
});

server.listen(8000, () => {
  console.log('Listening on port 8000');
});
