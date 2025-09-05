# docker-Tp1
TP1 docker

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker --version
Docker version 28.3.3, build 980b856

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete
Digest: sha256:a0dfb02aac212703bfcb339d77d47ec32c8706ff250850ecc0e19c8737b18567
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                          PORTS     NAMES
c7094972c556   hello-world   "/hello"   About a minute ago   Exited (0) About a minute ago             wizardly_hypatia

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker rm c7094972c556
c7094972c556

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration>docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    a0dfb02aac21   3 weeks ago   20.3kB

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker rmi a0dfb02aac21
Untagged: hello-world:latest
Deleted: sha256:a0dfb02aac212703bfcb339d77d47ec32c8706ff250850ecc0e19c8737b18567

EXERCICE 4
PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
a2da0c0f2353: Pulling fs layer
716cdf61af59: Pull complete
c3741b707ce6: Pull complete
e5d9bb0b85cc: Pull complete
14a859b5ba24: Pull complete
14e422fd20a0: Pull complete
b1badc6e5066: Pull complete
Digest: sha256:33e0bbc7ca9ecf108140af6288c7c9d1ecc77548cbfd3952fd8466a75edefe57
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                     NAMES
b66a35e82281   nginx     "/docker-entrypoint.…"   28 seconds ago   Up 28 seconds   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker stop mon_nginx 
mon_nginx
PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker rm mon_nginx 
>> ^C
PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> docker rm mon_nginx
mon_nginx

EXERCICE 5 :

-->création de app.py + du Dockerfile

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration> cd '.\TP docker\'
PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration\TP docker> docker build -t flask-hello .
[+] Building 24.1s (9/9) FINISHED                                                                         docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                      0.1s
 => => transferring dockerfile: 400B                                                                                      0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                       2.4s
 => [internal] load .dockerignore                                                                                         0.1s
 => => transferring context: 2B                                                                                           0.0s 
 => [1/4] FROM docker.io/library/python:3.11-slim@sha256:1d6131b5d479888b43200645e03a78443c7157efbdb730e6b48129740727c31  9.6s
 => => resolve docker.io/library/python:3.11-slim@sha256:1d6131b5d479888b43200645e03a78443c7157efbdb730e6b48129740727c31  0.0s 
 => => sha256:a27cb4be70170df84ec3045fb7d33b3eb7018cb39fc029037429d9f06362737f 14.64MB / 14.64MB                          4.4s 
 => => sha256:1961ca026b04e3e3720545ee5a8e05e60692056663c685c5d2437bf3ad9e6e08 249B / 249B                                0.5s 
 => => sha256:fcec5a125fd8f69ba9d5c3fd9ecf3810f95775d4d5694ed731adcdeae1cff909 1.29MB / 1.29MB                            1.0s 
 => => sha256:396b1da7636e2dcd10565cb4f2f952cbb4a8a38b58d3b86a2cacb172fb70117c 29.77MB / 29.77MB                          5.5s 
 => => extracting sha256:396b1da7636e2dcd10565cb4f2f952cbb4a8a38b58d3b86a2cacb172fb70117c                                 2.1s 
 => => extracting sha256:fcec5a125fd8f69ba9d5c3fd9ecf3810f95775d4d5694ed731adcdeae1cff909                                 0.3s 
 => => extracting sha256:a27cb4be70170df84ec3045fb7d33b3eb7018cb39fc029037429d9f06362737f                                 1.3s 
 => => extracting sha256:1961ca026b04e3e3720545ee5a8e05e60692056663c685c5d2437bf3ad9e6e08                                 0.0s 
 => [internal] load build context                                                                                         0.1s 
 => => transferring context: 220B                                                                                         0.0s 
 => [2/4] WORKDIR /app                                                                                                    1.0s 
 => [3/4] COPY app.py .                                                                                                   0.2s 
 => [4/4] RUN pip install --no-cache-dir flask                                                                            7.6s 
 => exporting to image                                                                                                    2.6s 
 => => exporting layers                                                                                                   1.6s 
 => => exporting manifest sha256:b101a6cdfb1d1d9eb3b2198e5948d80e80326dadcd5c83b50859b63aab96969e                         0.0s 
 => => exporting config sha256:e669d88c45088ecc21d39791af2e9ddec1c1662858935218ad550ec9cf40a62d                           0.0s 
 => => exporting attestation manifest sha256:46d67c79da30994c9f6306da1b89dfb2dca4e11312f6de9537aaf30dce4f87fa             0.1s 
 => => exporting manifest list sha256:6205f107ef05e3b9cb74b03beadfbee016f877d12d4c764b9749b08f18873735                    0.0s 
 => => naming to docker.io/library/flask-hello:latest                                                                     0.0s 
 => => unpacking to docker.io/library/flask-hello:latest

 PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration\TP docker> docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
flask-hello   latest    6205f107ef05   7 minutes ago   210MB
nginx         latest    33e0bbc7ca9e   3 weeks ago     279MB

PS C:\Users\lulu1\Documents\Importants\M2\docker\TP-int-gration\TP docker> docker run -p 5000:5000 flask-hello
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [05/Sep/2025 07:03:36] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [05/Sep/2025 07:03:36] "GET /favicon.ico HTTP/1.1" 404 -

Le testde l'application via : http://localhost:5000/ fonctionne bien
[a](./image.png)
