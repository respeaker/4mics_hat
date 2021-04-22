4MICs HAT for Raspberry Pi
========================

## Docker
To build the docker image, you need to upgrade the libseccomp2 library (bug identified in 12/2020)

1. wget http://ftp.fr.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.5.1-1_armhf.deb
2. wget http://ftp.fr.debian.org/debian/pool/main/libs/libseccomp/libseccomp-dev_2.5.1-1_armhf.deb
3. sudo dpkg -i  libseccomp2_2.5.1-1_armhf.deb libseccomp-dev_2.5.1-1_armhf.deb
4. rm *.deb
5. docker-docker-compose build