## Deployment means making your locally running API available on a server so that other people and applications can access it through a public URL.

For example, your local API runs at http://127.0.0.1:8000. After deployment, it might run at a URL such as https://your-api.example.com.


## Prepare your project
Create a folder with these files:

fastapi-project/

main.py  ------------------API code

requirements.txt--------Dependencies

Dockerfile------------Container setup


main.py

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My API is live!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

```

requirements.txt

```
fastapi
uvicorn[standard]
```


For a real project, pin and test dependency versions before deploying.


3. Create a Dockerfile


A Dockerfile tells Docker how to package and run your application.


```

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```

Understand the important parts:
- FROM selects the Python environment.
- WORKDIR sets the application directory.
- COPY copies your files into the image.
- RUN installs the dependencies.
- CMD starts the FastAPI server.
- 0.0.0.0 allows the server to accept connections through the container's network interface.


4. Build and run the Docker container
Make sure Docker Desktop is installed and running. In your project directory, execute:

```
docker build -t my-fastapi-api .
```


This builds a Docker image.
Then run it:

```
docker run --rm -p 8000:8000 my-fastapi-api
```

Open these URLs on your computer:
- Test the API
- Open Swagger UI
- Check API health
At this stage, the API is running in a container on your computer. It is not publicly deployed yet.


### Deploy it to the cloud
You have several options.
Platform	When to consider it
Google Cloud Run	Deploy a containerized API; a good option for learning cloud deployment
Render	A straightforward option for deploying a web service
AWS App Runner	Managed deployment for containerized web applications
Amazon EC2	More control over the server and its configuration


## Consider deploying application on the Google cloud


Go to Google Cloud Console.

Sign in with your Google account.

Create a new Google Cloud project or select an existing project.

Make sure billing is enabled for the project.


New customers may be eligible for $300 in free credits, but check the current terms and pricing before deploying.


### Step 4: Install Google Cloud CLI
On Windows, install the Google Cloud CLI.
After installation, open a new terminal and run:
gcloud init


Follow the prompts to sign in and select your Google Cloud project.


### Step 5: Deploy your API
For a beginner, you can deploy directly from your source code without manually building a Docker image. Google Cloud builds the container for you. 

Google Cloud Documentation



Open the terminal inside your fastapi-project folder, where main.py and requirements.txt are located.


Run:
```
gcloud run deploy saloni-fastapi-api --source .
```


#### Follow the prompts:
1. Enable any requested APIs by confirming when prompted.
2. Select asia-south1 for the Mumbai region if offered.
3. Confirm public access only if you want anyone to be able to call this demonstration API.
4. Wait for the build and deployment to finish.
Google Cloud will display a service URL when deployment succeeds.


### Step 6: Test your deployed API

Suppose Google Cloud gives you a URL like https://saloni-fastapi-api-xxxxx.a.run.app. This is only an example; your actual URL will be different.
Open these paths using your actual URL:


Path	Expected result
/	{"message": "My FastAPI API is live!"}
/health	{"status": "healthy"}
/docs	Interactive Swagger API documentation
If these work, congratulations — your first FastAPI REST API is deployed!


## Step 7: Check costs and security
- Check the Cloud Run pricing page.
- Set a budget alert in Google Cloud Billing.
- Do not commit API keys or database passwords to GitHub.
- Keep private APIs protected by authentication; public access is appropriate only for endpoints intended to be public.