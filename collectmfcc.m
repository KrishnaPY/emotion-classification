%collectmfcc.m
function [mfcoef]=collectmfcc(x,FS)
f=1:1:FS/2;
mel=2595*log10(1+f/700);
figure(1)
plot(f,mel)
%Uniform in mel frequency
s=mel(FS/2)/25;
%Identify the center frequency in normal scale.
COL=[];
for i=1:1:25
[p,r]=min(abs(mel-i*s));
COL=[COL f(r)];
end
COL=[0 COL]/max(COL);
figure(2)
%Create bank of filters
xrange=([0:1:999]/999);
for i=1:1:24
x1=COL(i):0.001:(COL(i+2)+COL(i))/2;
y1=(2/(COL(i+2)-COL(i)))*x1-(2/(COL(i+2)-COL(i)))*COL(i);
x2=(COL(i+2)+COL(i))/2:0.001:COL(i+2);
y2=(-2/(COL(i+2)-COL(i)))*x2+(2/(COL(i+2)-COL(i))*COL(i+2));
a=zeros(1,1000);
a(round(x1*999+1))=y1;
a(round(x2*999+1))=y2;
filter_col{i}=a;
plot(xrange,a)
hold on
end
sbs=fix(FS*25*10ˆ(-3));
ovs=fix(FS*10*10ˆ(-3));
mfcoef=blkproc(x,[1 sbs],[0 ovs],’obtainmfcc(x,P1)’,filter_col);
%obtainmfcc.m
function [res]=obtainmfcc(x,filter_col)
%Apply hammingwindow and followed by fft
y=hamming(length(x))’.*x;
x1=abs(fft(y,1998));
x2=x1(1:1:1000);
res1=log10(sum(abs(fft(y)).ˆ2));
res2=[];
for i=1:1:24
res2=[res2 sum((x2.*filter_col{i}).ˆ2)];
end
res3=log10(res2);
%Suppose the energy values are scaled by some constant number,
%taking log
%will have the corresponding DC shift. This is further removed
%using dct as follows.
res4=dct(res3);
res5=res4(2:1:13);
res6=diff(res5);
res7=diff(res6)
res=[res1 res5 res6 res7];