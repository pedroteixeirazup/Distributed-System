const Company = require('../models/Company');
const bcrypt = require('bcryptjs');

const salt = bcrypt.genSaltSync(10);

module.exports = {
    async store(req, res) {
        const { name, email, password, promotion } = req.body;
        
        const hash = bcrypt.hashSync(password, salt);

        const emailExist = await Company.findOne({email});

        if (emailExist)
            return res.status(400).json({ error: 'Email is in use'});
        
        const company = await Company.create({
            name,
            email,
            password: hash,
            promotion
        });

        company.password = undefined;

        return res.json({
            company
        });
    },

    async index(req, res) {
        const company = await Company.find();
        
        if (!company) 
            res.status(400).json({error:'Company not found'});
        
        return res.json(company);
    },

    async update(req, res) {
        const company = await Company.findById({_id: req.params.id});

        if (!company) 
            res.status(400).json({error:'Company not exist'});
        
        await Company.updateOne({ _id: req.params.id }, req.body);
        await company.save();

        return res.status(200).json({message:'Company updated'});
    },

    async delete(req, res) {
        const company = await Company.findByIdAndDelete({ _id: req.params.id });

        if (!company)
            res.status(400).json({ error: 'Company not exist' });
        
        res.send();
    }
}