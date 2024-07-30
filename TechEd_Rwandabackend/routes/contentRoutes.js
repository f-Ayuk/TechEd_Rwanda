const express = require('express');
const router = express.Router();
const { getCourses, getResources } = require('../controllers/contentController');

router.get('/courses', getCourses);
router.get('/resources', getResources);

module.exports = router;

