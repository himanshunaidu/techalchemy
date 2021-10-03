const express = require("express");
const router = express.Router();

const newsController = require("../controllers/news");

router.get("/", newsController.fetchNews);

module.exports = router;
