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


