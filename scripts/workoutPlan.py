# Change these to whatever model and text URL you want to use
WORKFLOW_ID = 'chat-gpt-4-turbo'
TEXT_FILE_URL = 'https://samples.clarifai.com/negative_sentence_12.txt'

############################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2


def workoutGen(RAW_TEXT_INPUT, PAT, USER_ID, APP_ID):

    print("generating workout")
    wokrout_filename = f"{RAW_TEXT_INPUT}.txt"

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)

    post_workflow_results_response = stub.PostWorkflowResults(
        service_pb2.PostWorkflowResultsRequest(
            user_app_id=userDataObject,  
            workflow_id=WORKFLOW_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            raw= RAW_TEXT_INPUT
                        )
                    )
                )
            ]
        ),
        metadata=metadata
    )
    if post_workflow_results_response.status.code != status_code_pb2.SUCCESS:
        print(post_workflow_results_response.status)
        raise Exception("Post workflow results failed, status: " + post_workflow_results_response.status.description)

    # We'll get one WorkflowResult for each input we used above. Because of one input, we have here one WorkflowResult
    workout_path = "C:\\Coding\\Github\\bodyBuild_Companion\\app\\generatedWorkout\\" + wokrout_filename

    results = post_workflow_results_response.results[0].outputs[0].data.text.raw

    with open(workout_path, 'w') as f:
        f.write(str(results))

    print("Workout Done!")
    
    return(workout_path)
