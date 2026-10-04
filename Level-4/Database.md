SQLAlchemy

SQLAlchemy is a popular Python library that provides ORM functionality.



| Letter | Meaning | Example     |
| ------ | ------- | ----------- |
| C      | Create  | Add user    |
| R      | Read    | Get user    |
| U      | Update  | Change user |
| D      | Delete  | Remove user |



db.add(user)       # Create
db.query(User)     # Read
db.commit()        # Save changes
db.delete(user)    # Delete