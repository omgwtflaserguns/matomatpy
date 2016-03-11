adminroleid = new ObjectId();
guestroleid = new ObjectId();

db.role.insert({
    _id: adminroleid,
    name: "Admin",
    rights: ["bb", "of", "ss", "dc", "sh", "cp", "ma", "mb"]
});

db.role.insert({
    name: "User",
    rights: ["bb", "dc", "sh", "cp"]
});

db.role.insert({
    _id: guestroleid,
    name: "Guest",
    rights: ["bb"]
});

db.user.insert({
    name: "admin",
    role: adminroleid,
    created: new Date(),
    password: "admin",
    balance: 0.0
});

db.user.insert({
    name: "guest",
    role: guestroleid,
    created: new Date(),
    password: "k4cg",
    balance: 0.0
});