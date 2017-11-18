%dctbasisdemo.m
%DCT bases plot for N=24
a=[1 zeros(1,23)]’;
col=dct(a)’;
b=dct(a’);
figure
subplot(6,4,1)
plot(col(:,1))
i=1;
for j=2:1:24
subplot(6,4,i)
plot(b)
a=circshift(a,1);
b=dct(a);
i=i+1;
col=[col;b’];
subplot(6,4,i)
plot(col(:,i))
end