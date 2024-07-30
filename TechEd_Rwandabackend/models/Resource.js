const mongoose = require('mongoose');

const ResourceSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  infoTime: {
    type: String,
    required: true,
  },
  infoTitle: {
    type: String,
  },
});

module.exports = mongoose.model('Resource', ResourceSchema);

