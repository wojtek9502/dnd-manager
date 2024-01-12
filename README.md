## DND Manager

### Requirements
- Python 3.10
- Docker >=  24.0.5
- docker-compose >= 2.23.3

### Install
1) Run commands:
```shell
python -m pip install virtualenv
make install-venv
make install

make up
make db-upgrade
```
2) Create .env file in main project dir. See .env.example

### Run
1) Start containers  
```shell
make up
```

### Test
1) 
```shell
make test
```

### Coverage
```shell
make coverage
```

## Develop
### pgadmin
1) Run pgadmin
```shell
make run-pgadmin
```
2) Go to 127.0.0.1
3) Email\password: admin@admin.com \ admin
4) Connect with db. Host: 127.0.0.1 Port: 5432 Login/password (see docker-compose.yaml)

### Migrations
1) Create migration file
```shell
make db-migration
```
2) Check migration file
3) Update database
```shell
make db-upgrade
```
