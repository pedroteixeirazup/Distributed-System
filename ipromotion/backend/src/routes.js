const express = require('express');
const CustomerController = require('./controllers/Customer');
const CompanyController = require('./controllers/Company');

const routes =  express.Router();

routes.post('/register', CustomerController.store);
routes.get('/register', CustomerController.index);
routes.put('/register/:id', CustomerController.update);
routes.delete('/register/:id', CustomerController.delete);
routes.post('/company', CompanyController.store);
routes.get('/company', CompanyController.index);
routes.put('/company/:id', CompanyController.update);
routes.delete('/company/:id', CompanyController.delete);



module.exports = routes;