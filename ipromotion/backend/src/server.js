const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const routes = require('./routes');
const dbconfig = require('./config/db.json');

const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server);

const axios = require('axios');

const port = 3333;

const connectedUsers = {};

io.on('connection', socket => {

    const { user } = socket.handshake.query;
    connectedUsers[user] = socket.id

    console.log("New client connected"), setInterval(
        () => getApiAndEmit(socket),
        100
      );

      socket.on("disconnect", () => console.log("Client disconnected"));
})

const getApiAndEmit = async socket => {
    try {
        const res = await axios.get('http://localhost:3333/company');
        socket.emit('promotion', res.data);
    } catch(error) {
        console.error(`Error: ${error.code}`);
    }
}

mongoose.connect(`mongodb+srv://${dbconfig.user}:${dbconfig.password}@omnistack-vlfdq.mongodb.net/test?retryWrites=true&w=majority`, {
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