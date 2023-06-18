
### 1. Application - 'math api'

Web service with the following endpoints:

/min - given list of numbers and a quantifier (how many) provides min number(s)

/max - given list of numbers and a quantifier (how many) provides max number(s)

/avg - given list of numbers calculates their average 

/median - given list of numbers calculates their median

/percentile - given list of numbers and quantifier 'q', compute the qth percentile of the list elements


#### Setup & Execution

Set up a virtual environment (optional but recommended)

```cd math-api-calculator/
pip install -r requirements.txt
python app.py
```

<img width="400" alt="Screenshot 2023-06-18 at 14 33 04" src="https://github.com/manasashanubhogue/sojern-home-assignment/assets/6822599/a03c7cef-f425-4888-b025-3dbd55d3406b">


#### Testing

```python -m unittest test_app.py```


![Screenshot 2023-06-18 at 14 44 09](https://github.com/manasashanubhogue/sojern-home-assignment/assets/6822599/82fac0db-f3fa-421b-9a13-c0622b0f320d)
