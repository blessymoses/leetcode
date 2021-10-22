## 12 Factor App
1. Codebase
    - Code is version controlled
    - One codebase tracked in revision control, many deploys
2. Dependencies
    - Explicitly declare and isolate the dependencies
3. Config
    - Store configurations in the environment
4. Backing Services
    - Treat backing resources as attached resources
5. Build, Release and Run
    - Strictly separate build and run stages
6. Processes
    - Execute the app as one or more stateless processes
7. Port Binding
    - Export services via port binding
8. Concurrency
    - Scale-out via the process model
9. Disposability
    - Maximize the robustness with fast startup and graceful shutdown
10. Dev/Prod parity
    - Keep development, staging and production as similar as possible
11. Logs
    - Treat logs as event streams
12. Admin processes
    - Run admin/management tasks as one-off processes

## Docker
### Containerization
- Containerization allows us to create an abstract representation of all the software applications.
- An image is created and any number of containers can be launched using the image, in any environment easily
### Docker
- Docker is a containerization tool or framework that allows us to package once and run anywhere.
- It implements the open container initiative standard and the docker image will have the entire infrastructure information along with the application itself.
### Docker components and workflow
- `Docker registry`: this is where all the docker images are stored centrally.
- `Docker Host` is the machine where docker engine is installed.
- `Docker client` gives the ability to run commands against the docker engine.
### Image Layers and Overlay
- A docker image is made up of multiple layers. It uses the concept of `Union File System` to integrate these layers together.
- When we pull an image, it pulls several layers, starting with the base kernel and then it will merge and all those layers are overlays one layer on top of another.
- When we pull the next time, it will pull only the layers that have changed.
### docker run
- Runs a command in a new container
- The docker run command first creates a writeable container layer over the specified image, and then starts it using the specified command.
- docker run is equivalent to the API /containers/create then /containers/(id)/start. 
