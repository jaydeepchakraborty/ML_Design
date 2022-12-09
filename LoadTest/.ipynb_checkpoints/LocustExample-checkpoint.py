'''
# First make sure the rest api is up and running

# from web interface (Running on http://127.0.0.1:8089)
locust -f LocustExample.py 
# from terminal
locust --config=test_config.conf
'''

'''
on_start: will be called by each thread upon starting
on_stop: will be called by each thread upon finishing
@task: action done by iteratively
@seq_task(n): give an order to the task execution
wait_time: time to wait between two task executions
task_set: defines which set of tasks
'''

from locust import TaskSet, task, HttpUser, between


class RestUserTaskSet(TaskSet):
    
    def get_headers(self):
        try:
            return {'content-type': 'application/json'}
        except Exception as e:
            raise e
            
    def get_payload(self):
        try:
            return {"msg": "this is post method"}
        except Exception as e:
            raise e
            
    def __init__(self, environment):
        super().__init__(environment)
        try:
            print("INIT")
            self.headers = self.get_headers()
            self.payload = self.get_payload()
        except Exception as e:
            raise e
    
    def on_start(self):
        try:
            print("START")
        except Exception as e:
            raise e
            
    def on_stop(self):
        try:
            print("STOP")
        except Exception as e:
            raise e
    
    @task
    def invoke_rest_api_post(self):
        try:
            with self.client.post(
                "/test_rest_post",
                json = self.payload,
                headers = self.headers,
                name = "locust rest api post"
            ) as resp_of_api:
                if resp_of_api.status_code == 200:
                    print("SUCCESS: \n" + str(resp_of_api.json()))
                else:
                    print("ERROR: \n" + resp_of_api.status_code)
        except Exception as e:
            raise e

    @task
    def invoke_rest_api_get(self):
        try:        
            with self.client.get(
                "/test_rest_get",
                headers = self.headers,
                name = "locust rest api get"
            ) as resp_of_api:
                if resp_of_api.status_code == 200:
                    print("SUCCESS: \n" + str(resp_of_api.json()))
                else:
                    print("ERROR: \n" + resp_of_api.status_code)
        except Exception as e:
            raise e




class RestUserBehavior(HttpUser):
    
    tasks = [RestUserTaskSet]
    wait_time = between(0.100, 1.500)