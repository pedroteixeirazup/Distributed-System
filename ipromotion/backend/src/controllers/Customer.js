const Customer = require('../models/Customer');
const bcrypt = require('bcryptjs');

const salt = bcrypt.genSaltSync(10);

module.exports = {
    async store(req, res) {
        const { name, email, password} = req.body;

        const hash = bcrypt.hashSync(password, salt);

        const emailExist = await Customer.findOne({email});

        if (emailExist) 
            return res.status(400).json({ error: 'Email is in use'});

        const customer = await Customer.create({
            name,
            email,
            password: hash,
        });

        customer.password = undefined;

        return res.json({
            customer
        });
    },

    async index(req, res) {
        const customers = await Customer.find();

        if (!customers) 
            return res.status(400).json({ error: 'Customer not found'});

        return res.json(customers);
    },

    async update(req, res) {
        const customer = await Customer.findById({_id: req.params.id});

        if (!customer) 
            res.status(400).json({error: 'Customer not exist'});
        
        await Customer.updateOne({ _id: req.params.id }, req.body);
        await customer.save();

        return res.status(200).json({message: 'Customer updated'});
    },

    async delete(req, res) {
        const customer = await Customer.findOneAndDelete({_id: req.params.id});

        if (!customer) 
            res.status(400).json({error: 'Customer not exist'});

        res.send();
    }


}