clear all; close all; clc;

data10 = csvread('AltitudeVsDriftUppperSection.csv',4,0);
data20 = csvread('AltitudeVsDriftUperSection20mph.csv',4,0);


resolution = 8; %MP
fovHorizontal = 48.8;%degrees
fovVertical = 62.2; %degrees
altitude = linspace(.0001,5500,1000); %ft
range = linspace(.0001, 2500,1001); %ft

numPixels = zeros(length(altitude),length(range));

for i = 1:length(altitude)
    for j = 1:length(range)
        numPixels(i,j) = sizeOfTarps(altitude(i),range(j),resolution,fovHorizontal,fovVertical);
    end
end

range1 = linspace(-2500+300,2500+300,2001);
range2 = linspace(-2500-300,2500-300,2001);
%+300 and -300 on the min and max of this manipulates location of tarps in
%relation to the launch pad
%two ranges to overlay different both +300 and -300 at the same time
for i = 1:length(altitude)
    for j = 1:length(range1)
        if (j<1001)
            numPixels2(i,j) = numPixels(i,1002-j);
        else
            numPixels2(i,j) = numPixels(i,j-1000);
        end
        if(sqrt(i^2 + (j-1001)^2) < 50)
            numPixels2(i,j) = NaN;
        end
    end
end
v = [300, 500, 800, 1200, 1700, 2300, 3000, 4000, 6000, 20000];
[C,h] = contour(range1,altitude,numPixels2,v); %someone please epxlain wtf this is?
hold on;
[C,h] = contour(range2,altitude,numPixels2,v);
plot(data10(:,2),data10(:,1),'Linewidth',2,'Color','b')
plot(data20(:,2),data20(:,1),'Linewidth',2,'Color','r')
clabel(C,h,v)
xlabel('Downrange Distance [ft]')
ylabel('Altitude [ft]')
legend('Contours of Tarp Size in Pixels','10 MPH Wind Trajectory','20 MPH Wind Trajectory')
title('Estimated Number of Pixels Occupied by Tarp')
set(gca,'FontSize',16)