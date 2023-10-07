from gradio_client import Client

client = Client("http://k8s-default-classifi-5fc46bb387-295012219.ap-south-1.elb.amazonaws.com/")

for i in range(10000):
    result = client.predict(
        "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",	# str (filepath or URL to image)
        api_name="/predict"
    )