# Utils

pymysql wrapper for execute sql with pandas dataframe

## Installation
```shell script
# In your shell
pip install -U git+https://github.com/alpha-trading/utils.git
# In colab
!pip install -U git+https://github.com/alpha-trading/utils.git
```

## Usage
```python
from utils import Executor

executor = Executor("mysql://user:password@db.url.com:3306/dbname")
# or use env var (env name: DATABASE_URL)
data_frame = executor.sql("SELECT data_candleday.*, ticker.ticker FROM data_candleday INNER JOIN data_ticker as ticker ON ticker.id = data_candleday.ticker_id LIMIT 100;")
print(data_frame)
```

## Contribution

Use [pre-commit](https://pre-commit.com/)

```shell
pre-commit install
```

## Version up
Run command after edit pyproject.toml's version
```shell script
$ make setup
$ git add pyproject.toml
$ git add setup.py
$ git commit
$ git push origin master
```
