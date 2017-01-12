clear all; close all; clc;

data10 = csvread('AltitudeVsDriftUppperSection.csv',4,0);
data20 = csvread('AltitudeVsDriftUperSection20mph.csv',4,0);
data0 = csvread('AltitudeVsDriftUpppperSection0mph.csv',4,0);
%data0 is the zero mph wind data set

%VERY IMPORTANT! This is the horizontal offset of the tarp with respect to
%the rocket.
positionOfTarp = 300; %ft


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

range = linspace(-2500,2500,2001);

for i = 1:length(altitude)
    for j = 1:length(range)
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
[C,h] = contour(range,altitude,numPixels2,v);
hold on;

clear i
clear j

%the ranges on each dataset are stored in these variables
range0 = data0(:,2);
range10 = data10(:,2);
range20 = data20(:,2);

%these three for loops shift each range value for data0, data10 and data20 by
%positionOfTarp. The second and third loops effectively move the trajectory
%plots to the left or right. range0 was adjusted as a necessity for the
%table

for j = 1:length(range0)
    range0(j) = range0(j) + positionOfTarp;
end

for i = 1:length(range10)
    range10(i) = range10(i) + positionOfTarp;
end

for j = 1:length(range20)
    range20(j) = range20(j) + positionOfTarp;
end


plot(range10,data10(:,1),'Linewidth',4)
plot(range20,data20(:,1),'Linewidth',4)
clabel(C,h,v)
xlabel('Downrange Distance [ft]')
ylabel('Altitude [ft]')
legend('Contours of Tarp Size in Pixels','10 MPH Wind Trajectory','20 MPH Wind Trajectory')
title('Estimated Number of Pixels Occupied by Tarp (0ft tarp offset)')
set(gca,'FontSize',16)
%testing github


FinalTable = zeros(length(data0),5);
%FinalTalbe will be the "look up table" and will be structured as such:
%It will have 652 rows and 5 columns
%Since the 0 mph data set had the fewest number of altitutde samples (649
%samples), this table must have 649 rows for each sample and 3 rows for appropriate labels
%Each column is explained below

%The first column will contain each of the altitude values from the data0 data set
%(note the altitude values are the SAME for the 0, 10, and 20 mph data
%sets. Choosing the data0 data set was completely arbitrary)

%BOTH the second and third columns will contain the pixel sizes for a zero ft
%horizontal tarp offset. They will contain the pixel sizes for the data0
%and data20 datasets, RESPECTIVELY 

%BOTH The fourth and fifth columns will contain the pixel sizes for a +300
%ft horizontal tarp offset. They will contain the pixel sizes for the data0
%and data20 datasets, RESPECTIVELY


%this for loop makes the first 3 rows of FinalTable NaN so column labels can be
%added in excel
i = 1;
j = 1;
for j = 1:5
    for i = 1:3
        FinalTable(i,j) = NaN;
    end
end

%this is where the actual filling in of the table is done!
%i represents a row and j represents a column of the final talbe
for i = 4:length(data0)+3
    for j = 1:5
        %if the first column, fill it with the altitude values from data0
        if j == 1
            FinalTable(i,j) = data0(i-3);
        
        %else if the second column, fill it with the pixel size at the
        %given altitude with ZERO WIND (zero ft horizontal tarp offset)
        elseif j == 2
            FinalTable(i,j) = sizeOfTarps(data0(i-3,1),data0(i-3,2),resolution,fovHorizontal,fovVertical);
        
        %else if the third column, fill it with the pixel size at the
        %given altitude with 20 MPH WIND (zero ft horizontal tarp offset)
        elseif j == 3
            FinalTable(i,j) = sizeOfTarps(data20(i-3,1),data20(i-3,2),resolution,fovHorizontal,fovVertical);
        
        %else if the second column, fill it with the pixel size at the
        %given altitude with ZERO WIND (300 ft horizontal tarp offset) 
        elseif j == 4
            FinalTable(i,j) = sizeOfTarps(data0(i-3,1),range0(i-3),resolution,fovHorizontal,fovVertical);
            
        %OTHERWISE, we must be in the fifth and final column, which means
        %we must fill it with the pixel size at the given altitude with 20
        %MPH WIND (300 ft horizontal tarp offset)
        else
            FinalTable(i,j) = sizeOfTarps(data20(i-3,1),range20(i-3),resolution,fovHorizontal,fovVertical);
        end
    end
end
                
            
    
