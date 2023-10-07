import random
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # You can adjust the wait time as needed

    @task
    def classify_image(self):
        url = "/classify-imagenet"

        # Prepare a random image file from your local directory
        files = {'image': ("result (8).jpeg", open(f'/Users/satyajitghana/Downloads/result (8).jpeg', 'rb'), 'image/jpeg')}

        # Make a POST request to the API
        self.client.post(url, files=files)

