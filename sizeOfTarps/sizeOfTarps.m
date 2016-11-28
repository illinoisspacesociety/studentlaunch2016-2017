function [totalPixels] = sizeOfTarps(altitude, range, resolution, fovHorizontal, fovVertical)
%assume tarps are oriented such that they appear as a trapezoid on the ground
%assume whole tarp is in frame
%assume camera is oriented with larger FOV vertical

resolution = resolution*1e6;
aspectRatio = fovVertical/fovHorizontal;
verticalPixels = sqrt(resolution/aspectRatio);
horizontalPixels = verticalPixels*aspectRatio;

distToFront = sqrt(altitude^2 + (range-20)^2);
distToBack = sqrt(altitude^2 + (range+20)^2);

circumferenceSphereFront = 2*pi*distToFront;
circumferenceSphereBack = 2*pi*distToBack;

frontLength = circumferenceSphereFront*fovHorizontal/360;
backLength = circumferenceSphereBack*fovHorizontal/360;

pixelsFront = horizontalPixels*40/frontLength;
pixelsBack = horizontalPixels*40/backLength;

dotProductLength = 40*cosd(atand(range/altitude));

frontDepth = circumferenceSphereFront*fovVertical/360;

pixelsDepth = verticalPixels*dotProductLength/frontDepth;

totalPixels = (pixelsFront + pixelsBack)*pixelsDepth/2;

end