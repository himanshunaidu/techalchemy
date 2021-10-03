const bcrypt = require("bcryptjs");

const User = require("../models/user");

const signup = (req, res, next) => {
  bcrypt.hash(req.body.password, 10).then((hash) => {
    const newUser = new User(req.body.name, req.body.email, hash);
    newUser
      .save()
      .then((users) => {
        res.status(200).json({
          status: "Success",
          hash: hash,
        });
      })
      .catch((err) => {
        res.status(400).json({
          status: `Failure. ${err}`,
        });
      });
  });
};

const login = (req, res, next) => {
  User.fetchUser(req.body.name)
    .then((user) => {
      bcrypt.compare(req.body.password, user.password, (err, response) => {
        console.log(response);
        if (err) {
          return res
            .status(401)
            .json({ success: false, message: "Unexpected Error" });
        }
        if (response) {
          User.updateUserLogged(user.name, true).then(
            (message) => {
              return res.status(200).json({ success: true });
            },
            (err) => {
              return res
                .status(200)
                .json({ success: false, message: "Error logging in" });
            }
          );
        } else {
          return res
            .status(401)
            .json({ success: false, message: "Passwords do not match" });
        }
      });
    })
    .catch((err) => {
      return res
        .status(401)
        .json({ success: false, message: "User not found" });
    });
};

const logout = (req, res, next) => {
  User.fetchUser(req.body.name)
    .then((user) => {
      User.updateUserLogged(user.name, false).then(
        (message) => {
          return res.status(200).json({ success: true });
        },
        (err) => {
          return res
            .status(200)
            .json({ success: false, message: "Error logging out" });
        }
      );
    })
    .catch((err) => {
      return res
        .status(401)
        .json({ success: false, message: "User not found" });
    });
};

module.exports = { signup: signup, login: login, logout: logout };
