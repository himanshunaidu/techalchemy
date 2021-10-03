const fs = require("fs");
const path = require("path");

const pathUtil = require("../util/path");

//Helper Function
const contactPath = path.join(pathUtil.mainPath, "data", "users.json");
const readPromiseHelper = (callback) => {
  fs.readFile(contactPath, (err, users) => {
    if (err) {
      callback(new Map());
    } else {
      let obj = JSON.parse(users);
      callback(new Map(Object.entries(obj)));
    }
  });
};

class User {
  constructor(name, email, password) {
    this.name = name;
    this.email = email;
    this.password = password;
    this.logged = false;
  }

  save() {
    //We use readFile then writeFile instead of appendFile, because we need to store an array
    return new Promise((resolve, reject) => {
      readPromiseHelper((users) => {
        if (users.get(this.name)) {
          reject("User exists");
        } else if (
          !/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(this.email)
        ) {
          reject("Invalid email");
        } else {
          users.set(this.name, this);
          console.log(users);
          fs.writeFile(
            contactPath,
            JSON.stringify(Object.fromEntries(users)),
            (err) => {
              if (err) {
                console.log("Error", err);
              }
              resolve("Success");
            }
          );
        }
      });
    });
  }

  static async updateUserLogged(name, logged) {
    return new Promise((resolve, reject) => {
      readPromiseHelper((users) => {
        const user = users.get(name);
        if (user) {
          user.logged = logged;
          fs.writeFile(
            contactPath,
            JSON.stringify(Object.fromEntries(users)),
            (err) => {
              if (err) {
                console.log("Error", err);
              }
              resolve("Success");
            }
          );
        } else {
          reject("User not Found");
        }
      });
    });
  }

  static async fetchUser(name) {
    return new Promise((resolve, reject) => {
      readPromiseHelper((users) => {
        const user = users.get(name);
        if (user) {
          resolve(user);
        } else {
          reject("User not Found");
        }
      });
    });
  }
}

module.exports = User;
