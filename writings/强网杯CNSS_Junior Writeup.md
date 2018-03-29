#强网杯CNSS_Junior Writeup

## Misc

### 0x01 签到

####操作内容

直接交

####FLAG值

flag{welcome_to_qwb}

### 0x02 Welcome

####操作内容

丢进stegsolve， 选择隐写分析， 讲图⽚分成两份， 其中⼀份右移100像素可以看到flag

####FLAG值

QWB{W3lc0me}

### 0x03 问卷

####操作内容

填写问卷

####FLAG值

flag{强网杯强国梦}

## Web

### 0x04 web签到

####操作内容

第一关

0e绕过

"param1": "QNKCDZO",

"param2": "240610708"

第二关

数组绕过

"param1[]": "1",

"param2[]": "2"

第三关

md5碰撞

"param1": b'Oded Goldreich\nOded Goldreich\nOded Goldreich\nOded Go' + unhexlify('d8050d0019bb9318924caa96dce35cb835b349e144e98c50c22cf461244a4064bf1afaecc5820d428ad38d6bec89a5ad51e29063dd79b16cf67c12978647f5af123de3acf844085cd025b956'),

"param2": b'Neal Koblitz\nNeal Koblitz\nNeal Koblitz\nNeal Koblitz\n' + unhexlify('75b80e0035f3d2c909af1baddce35cb835b349e144e88c50c22cf461244a40e4bf1afaecc5820d428ad38d6bec89a5ad51e29063dd79b16cf6fc11978647f5af123de3acf84408dcd025b956')

}

####FLAG值

QWB{s1gns1gns1gnaftermd5}

## Reverse

### 0x05 picturelock

####操作内容

先查壳，无壳。拖进Android killer，发现资源文件里面有lib文件夹，里面有libnative.so文件，那么肯定有jni层逆向。然后反汇编看下java代码，发现有个enc，把so文件拖ida  
关键函数 int __fastcall sub_1A48(char *filename, char *a2) 一个是文件路径，一个是输出路径
看代码 其实在 stream = fopen(v4, (const char *)&unk_3F5C); 之前，都是得到sig的算法，dump出来得到：f8c49056e4ccf9a1
1e090eaf471f418d 下面是解密过程了，看了好久好久……，最后发现是个aes…… 尴尬果然还是逆东西逆的太少了，用python的pyCrypto库跑一下就好，源文件是assets目录里面flag.jpg.lock。

####FLAG值

flag{!T_!S_a_s!Mpi3_PLctuRe_LOC33r}

### 0x06 simplecheck

####操作内容

题目如名，就是simple，是个apk，没有lib，就是native层的逆向，反汇编成java代码，就是把输入的数据做了处理过后，和内存中的数据比对一下。关键代码是

```java
if((a[i]!=b[i]*ans[i]*ans[i]+c[i]*ans[i]+d[i])|| (a[i+1]!=b[i]*ans[i+1]*ans[i+1]+c[i]*ans[i+1]+d[i]))
```

观察发现：本次循环的后一个一元二次方程和下一次循环的第一个一元二次方程构成了一个一元二次方程组，以此来保证唯一解，同理，把数据拷出来，用python的numpy库中的poly1d([a,b,c]) 解一下方程就好。

####FLAG值

flag{MAth_i&_GOOd_DON7_90V_7hInK?}



