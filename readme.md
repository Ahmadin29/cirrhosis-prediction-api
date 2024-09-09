## HOW TO USE

### 1. Clone the repo
```bash
git clone git@github.com:Ahmadin29/cirrhosis-prediction-api.git
```

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Run the app
```bash
uvicorn main:app --reload
```
or
```bash
fastapi dev main.py 
```

### 3. Test the app

#### 3.1 Using postman
- Open postman
- Click on import
- Choose the cirrhosis-prediction-api.postman_collection.json file
- Click on import
- Go to Predict request
- Click on the body tab
- Click on raw
- Edit the request body
- Click on send

#### 3.2 Using curl
```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "age": 30, "city": "New York"}' http://127.0.0.1:8000/predict
```