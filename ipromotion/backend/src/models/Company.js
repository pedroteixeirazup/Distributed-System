const { Schema, model } = require('mongoose');

const CompanySchema = new Schema({
    name: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
    },
    password: {
        type: String,
        required: true,
        select: false,
    },
    promotion: {
        type: String
    }
}, {
    timestamps: true
});

module.exports = model('Company', CompanySchema);