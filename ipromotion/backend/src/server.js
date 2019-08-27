const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const routes = require('./routes');
const dbconfig = require('./config/db.json');

const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

const Company = require('./models/Company');

const port = 3333;

const connectedUsers = {};

io.on('connection', socket => {
    console.log('a user connect');

    const { user } = socket.handshake.query;
    connectedUsers[user] = socket.id

    socket.on('client message',  (msg) => {
        console.log('Cliente: ' + msg);
    })

    console.log(connectedUsers, socket.id);
    var  person = {name: 'PEDRO', age: 22 }
    socket.broadcast.emit('promotion', person);
})

mongoose.connect(`mongodb+srv://${dbconfig.user}:${dbconfig.password}@cluster0-crbfw.mongodb.net/test?retryWrites=true&w=majority`, {
    useNewUrlParser: true,
    useFindAndModify: true
})

app.use((req, res, next) => {
    req.io = io;
    req.connectedUsers = connectedUsers;

    return next();
})
app.use(cors());
app.use(express.json());
app.use(routes);


server.listen(port ,'0.0.0.0', () => console.log('App running on port ' + port));