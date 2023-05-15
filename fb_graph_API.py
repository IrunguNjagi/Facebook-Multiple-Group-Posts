import facebook 

#Sign up for Facebook Developer Account and get access token
graph = facebook.GraphAPI(access_token="")


#Define a list of facebook groups to send messages to
group_ids = ['GROUP_1','GROUP_2','GROUP_3']

#Define message to be sent to groups

message = "ENTER YOUR CUSTOM MESSAGE HERE"

#Loop through each group id and post the given message
for group_id in group_ids:
    graph.put_object(parent_object=group_id, connection_name= "feed", message = message)
