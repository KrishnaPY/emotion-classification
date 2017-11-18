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