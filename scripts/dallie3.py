
######################################################################################################
# In this section, we set the user authentication, user and app ID, model details, and the URL of 
# the text we want as an input. Change these strings to run your own example.
######################################################################################################

# Change these to whatever model and text URL you want to use
WORKFLOW_ID = 'Image_Generation'
TEXT_FILE_URL = 'https://samples.clarifai.com/negative_sentence_12.txt'
#RAW_TEXT = 'A chibi bodybuilding robot companion'

#RAW_TEXT_INPUT = input("What is your prompt?")
#image_filename = f"{RAW_TEXT_INPUT}.jpg"



############################################################################
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE TO RUN THIS EXAMPLE
############################################################################

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2

import base64


def imgGen(RAW_TEXT_INPUT, PAT, USER_ID, APP_ID) -> int:

    image_filename = f"{RAW_TEXT_INPUT}.jpg"

    channel = ClarifaiChannel.get_grpc_channel()
    stub = service_pb2_grpc.V2Stub(channel)

    metadata = (('authorization', 'Key ' + PAT),)

    userDataObject = resources_pb2.UserAppIDSet(user_id=USER_ID, app_id=APP_ID)
    print('Intialization complete')

    post_workflow_results_response = stub.PostWorkflowResults(
        service_pb2.PostWorkflowResultsRequest(
            user_app_id=userDataObject,  
            workflow_id=WORKFLOW_ID,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(
                        text=resources_pb2.Text(
                            #url=TEXT_FILE_URL
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
    results = post_workflow_results_response.results[0].outputs[0].data.image.base64

    #image_filename = f"gen-image1.jpg"
    image = None
    # For Computer 
    image_path = "C:\\Coding\\Github\\bodyBuild_Companion\\images\\" + image_filename

    #For Laptop
    #image_path = "C:\\Users\\heroa\\Documents\\Code\\GIthub\\bodyBuild_Companion\\images" + image_filename
    with open(image_path, 'wb') as f:
        f.write(results)
        image = (f.write(results))

    print(type(image))

    return (image_path)

# Each model we have in the workflow will produce one output.
    '''
for output in results.outputs:
    model = output.model

    print("Predicted concepts for the model `%s`" % model.id)
    for concept in output.data.concepts:
        print("	%s %.2f" % (concept.name, concept.value))

# Uncomment this line to print the full Response JSON
print(results)
'''
