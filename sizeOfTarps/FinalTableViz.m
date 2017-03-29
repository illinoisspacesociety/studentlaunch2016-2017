%YOU MUST RUN EnhancedCallSizeOfTarps BEFORE YOU RUN THIS!!!!!!!!!!
%This script will produce a plot of the min and max pixel sizes of the tarp
%in each row of FinalTable as a continuous function of altitude

clear i

%SmallestInRow will contain the minimum of each row of
%FinalTableWithoutAltitudes
%LargestInRow will contain the maximum of each row of
%FinalTableWithoutAltitudes
%Note, we will be taking the log of these later to make the plot look nicer
SmallestInRow = zeros(1,length(FinalTable)-3);
LargestInRow = zeros(1,length(FinalTable)-3);

%creates new variable which is FinalTable without the altitude column
FinalTableWithoutAltitudes = FinalTable(:,2:5);

%this for loop does most of the work
%it finds the min and max of each row of FinalTableWithoutAltitudes
%it then take the min and max and places it in the appropriate place in
%SmallestInRow and LargestInRow respectively
for i = 4:length(FinalTable)
    SmallestInRow(i-3) = min(FinalTableWithoutAltitudes(i,:));
    LargestInRow(i-3) = max(FinalTableWithoutAltitudes(i,:));
end

Altitudes = FinalTable(4:length(FinalTable),1);

%The pixel numbers can get quite large. Plotting the raw numbers versus
%altitude didn't look nice at all. Here, we take the log of the
%SmallestInRow and LargestInRow to make the numbers easier to deal with
LogOfSmallestInRow = log(SmallestInRow);
LogOfLargestInRow = log(LargestInRow);

%here the plots of log(apparent pixel size) versus altitude are generated.
%the min and max log(apparent pixel size) plots are superimposed on
%eachother.
%the subplot function is used to generate two separate plots in the same
%figure: the first being the rocket's ascent and the second the decent

hFig = figure(1)

%ascent subplot
%the number 382 is position in Altitudes where the max altitude is
subplot(1,2,1);
plot(Altitudes(1:382), LargestInRow(1:382), 'b','linewidth',2)
hold on
plot(Altitudes(1:382), SmallestInRow(1:382), 'g','linewidth',2)

set(gca,'yscale','log')

title('Ascent');
xlabel('Altitude [ft]')
ylabel('Size of Tarp in Image [Pixels]')
legend('Maximum Tarp Size','Minimum Tarp Size')
set(gca,'fontsize',14)
axis([0 5400 10^2 10^8])
%decent subplot
subplot(1,2,2);

plot(Altitudes(382:length(Altitudes)), LargestInRow(382:length(LargestInRow)), 'b','linewidth',2)
hold on
plot(Altitudes(382:length(Altitudes)), SmallestInRow(382:length(SmallestInRow)), 'g','linewidth',2)

title('Descent');
xlabel('Altitude [ft]')
ylabel('Size of Tarp in Image [Pixels]')
legend('Maximum Tarp Size','Minimum Tarp Size')
set(gca,'fontsize',14)
set(gca,'yscale','log')
set(gca, 'xdir','reverse')
axis([0 5400 10^2 10^8])
set(gcf,'units','inches')
set(hFig,'Position',[2 1 9.5 5])