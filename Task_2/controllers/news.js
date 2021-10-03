const axios = require("axios");
// import fetch from "node-fetch";

const newsUtils = require("../util/newsAPI");

const fetchNews = (req, res, next) => {
  console.log(req.query.search);
  res.status(200).json({ message: "Received request" });
};

module.exports = { fetchNews: fetchNews };
