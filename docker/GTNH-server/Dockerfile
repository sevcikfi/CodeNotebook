FROM openjdk:8u342-jdk-slim

WORKDIR /data

#update and download wget and unzip

RUN apt update && \
    apt update -y && \
    apt install -y \
    wget unzip

#RUN ["apt", "update"]
#RUN ["apt", "upgrade", "-y"]
#RUN ["apt-get", "install", "wget", "unzip", "-y"]

# download the server
RUN ["wget", "-O", "GTNH-2.2.8.zip", "http://downloads.gtnewhorizons.com/ServerPacks/old/GT_New_Horizons_2.2.8_SERVER.zip"]
# unzip it
RUN ["unzip", "GTNH-2.2.8.zip", "-d", "."]

RUN echo "eula=true" > eula.txt

#CMD  java -Xms6G -Xmx6G -XX:+UseStringDeduplication -XX:+UseCompressedOops -XX:+UseCodeCacheFlushing -Dfml.readTimeout=180 -jar forge-1.7.10-10.13.4.1614-1.7.10-universal.jar nogui
#CMD ["bash", "startserver.sh"]
CMD ["bash"]