max_horizontal_speed=6.7;
downward_velocity=-4.57;
n=100;
g=-9.81;

horizontal_velocity=linspace(0,max_horizontal_speed,n);
CofMH=11*0.0254;
leg_length=12*0.0254;
diameter=6*0.0254;
leg_angle=deg2rad(12);
circum_rad_o_base=(diameter/2)+leg_length*cos(leg_angle);
inscrib_rad_o_base=circum_rad_o_base/sqrt(2);

totHofCofM=CofMH+leg_length*sin(leg_angle);
Psi=atan(totHofCofM/inscrib_rad_o_base);
psia=rad2deg(Psi);
theta_tip_no_v_x=90-psia;
L=sqrt(totHofCofM^2+inscrib_rad_o_base^2);

angles = linspace(0,90);
terminalAngle = ones(1,length(horizontal_velocity))*90;
success = zeros(length(horizontal_velocity),length(angles));

for i = 1:length(horizontal_velocity)
    for j = 1:length(angles)
        if((horizontal_velocity(i)*sind(angles(j)))^2/2 < 9.81*L*cosd(angles(j)))
            terminalAngle(i) = angles(j);
        end
    end
    terminalAngle(i) = terminalAngle(i)-90+theta_tip_no_v_x; 
    if(terminalAngle(i) < 0)
        terminalAngle(i) = 0;
    end
end



% syms x;
% syms theta;
% syms y;
% Sideone=symfun(sqrt(abs((2*g*(sin(Psi+theta_tip_no_v_x)-sin(Psi+theta)))/L)),theta);
% sz=size(horizontal_velocity);
% V=zeros(sz);
% V_angle=zeros(sz);
% for i=1:+1:n
%     V(i)=sqrt(horizontal_velocity(i)^2+downward_velocity^2);
%     V_angle(i)=atan(downward_velocity/horizontal_velocity(i));
% end
% Thetas=zeros(sz);
% Thetas(1)=theta_tip_no_v_x
% for i=2:+1:n
%     Sidetwo=symfun(abs((cos(V_angle(i)+deg2rad(90)-Psi-theta)*V(i))/L),theta);
%     Thetas(i)=rad2deg(vpasolve(Sidetwo==Sideone,theta,[0 theta_tip_no_v_x]))
% end
figure
plot(horizontal_velocity,terminalAngle)