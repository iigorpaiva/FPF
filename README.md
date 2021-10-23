# FPF Full Stack Test

This CRUD project was created to simulate some investiments based on each project created and persisted on database.

## Technologies: 

- `FRONT-END: BootstrapCDN;`
- `BACK-END: Python 3.8.10, FLASK 1.1.1;`
- `Database: SQLite;`

### Conditions: 

- `Integer and numeric fields cannot contain letters or symbols;`
- `If the investment amount is less than the project value, the system must display an error message.;`
- `The investment return calculation must consider the risk and value that will be invested. If the project risk is low=0, the return value should be 5% of the investment value. If the project risk is medium=1, the return value should be 10% the value of the investment. If the project risk is high=2, the return value should be 20% of the investment value.`

#### How to run: 

- `export FLASK_APP=app`
- `flask run`