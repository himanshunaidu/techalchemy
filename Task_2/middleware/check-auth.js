const User = require("../models/user");
const bcrypt = require("bcryptjs");

// Export a function and not a constant, for a middleware
module.exports = (req, res, next) => {
  User.fetchUser(req.body.name)
    .then((user) => {
      if (!user.logged) {
        return res
          .status(401)
          .json({ success: false, message: "User not logged in" });
      }
      next();
    })
    .catch((err) => {
      return res
        .status(401)
        .json({ success: false, message: "User not found" });
    });
  next();
};
