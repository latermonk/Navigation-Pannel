
1. Launch a unbuntu instance
```
multipass launch --name abc --bridged
```
2. test
```
wget -N https://gitlab.com/Misaka-blog/warp-script/-/raw/main/files/warp-yxip/warp-yxip.sh && bash warp-yxip.sh
```
3. change ep on eireguard

4. clean
```
multipass delete  abc && mp purge
```