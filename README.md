
# Svalbard

Your one stop password manager and strength checker. This password manager stores your password encrypted with added device secret and you only have to remeber the MASTER PASSWORD.


## Deployment

To deploy this project using docker, copy the docker-compose file and run

```bash
  docker-compose -f <file-name> up -d 
```
Run the svalbard container
```bash
  docker exec -it svalbard bash
```
#### Configure your MASTER PASSWORD
```bash
  python arsenal/config.py
```
#### Now, follow the USAGE steps

## Installation

You need to have mariadb and python3 installed to run this
### Linux
```bash
sudo apt install python3-pip
```
### MariaDB
#### Install MariaDB on linux with apt
```bash
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 0xcbcb082a1bb943db
sudo add-apt-repository 'deb http://ftp.osuosl.org/pub/mariadb/repo/5.5/ubuntuprecise main'
sudo apt-get update
sudo apt-get install mariadb-server
```

#### Create user 'svalbard' and grant permissions

* Login to mysql as root

    ```sudo mysql -u root```

* Create User

    ```CREATE USER 'svalbard'@localhost IDENTIFIED BY 'password';```

* Grant privileges

    ```GRANT ALL PRIVILEGES ON *.* TO 'svalbard'@localhost IDENTIFIED BY 'password';```

### Windows

### MariaDB Installation

Follow these instructions to install MariaDB on Windows
Create user and grant privileges

* Navigate to MariaDB bin directory

  ```C:\Program Files\MariaDB\bin```

* Login as root with the password you chose while installation

  ```mysql.exe -u root -p```

* Create user

  ```CREATE USER 'svalbard'@localhost IDENTIFIED BY 'password';```

* Grant privileges

  ```GRANT ALL PRIVILEGES ON *.* TO 'svalbard'@localhost IDENTIFIED BY 'password';```
## Run Locally

Clone the project

```bash
  git clone https://github.com/AlienwareSec/svalbard.git
```

Go to the svalbard directory

```bash
  cd svalbard
```

Install requirements

```bash
  pip install -r requirements.txt
```

#### Configure
You need to first configure the password manager by choosing a MASTER PASSWORD. This config step is only required to be executed once.

```bash
  python config.py
```


## Usage/Examples

```python
python svalbard.py -h
usage: svalbard.py [-h] [-s Site] [-u Username] [-e EMAIL] option

Description

positional arguments:
  option                (a)dd / (e)xtract / (s)trength

optional arguments:
  -h, --help            show this help message and exit
  -s NAME, --name NAME   Site name
  -u USER, --user USER   Username
  -e EMAIL, --mail EMAIL Email
```


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pawanngambhir/)

