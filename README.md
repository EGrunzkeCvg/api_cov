`pytest tests/ --cov=api_cov`
```
======================== test session starts ========================
platform win32 -- Python 3.7.4, pytest-5.3.4, py-1.8.1, pluggy-0.13.1
rootdir: C:\dev\pyspace\api_cov
plugins: asyncio-0.10.0, cov-2.8.1, mock-2.0.0
collected 1 item

tests\test_app.py .                                             [100%]

----------- coverage: platform win32, python 3.7.4-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
api_cov\__init__.py           0      0   100%
api_cov\app.py                9      1    89%
api_cov\routes\items.py      20      6    70%
---------------------------------------------
TOTAL                        29      7    76%
```

`pytest tests/ --cov=api_cov --cov-report=html`
```
======================== test session starts ========================
platform win32 -- Python 3.7.4, pytest-5.3.4, py-1.8.1, pluggy-0.13.1
rootdir: C:\dev\pyspace\api_cov
plugins: asyncio-0.10.0, cov-2.8.1, mock-2.0.0
collected 1 item

tests\test_app.py .                                            [100%]

----------- coverage: platform win32, python 3.7.4-final-0 -----------
Coverage HTML written to dir htmlcov
```
