import docker
client = docker.from_env()

contList = client.containers.list()

for contId in contList :
    print(" Container id is " + contId.id[0:11])
    print("Name: " + contId.name)
    print("Status: " + contId.status)

