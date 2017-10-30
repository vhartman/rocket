clc; close all; clear all;

%%

x0 = [0; 0; 0; 0; 0; 0; 200];

[t, x] = ode45(@(t,x)rocket(t,x), [0, 1000], x0);

figure(1)
subplot(2,2,1)
plot(t, x(:, 5))

subplot(2,2,2)
plot(t, x(:, 6))

subplot(2,2,3)
plot(t, x(:, 1))

subplot(2,2,4)
plot(t, x(:, 2))

figure(2)
subplot(2,1,1)
plot(t, 0.005*(x(:, 1)-0.0005));

subplot(2,1,2)
u = zeros(size(t));
for i=1:length(t)
    if x(i, 7) > 100
        u(i) = (x(i,7))/100;
    end
end
plot(t, u);

figure(3)
plot(x(:, 3), x(:, 5))
hold on
% plot rectangles separately
for i=1:size(t, 1)
    if (mod(i, 20) == 0 || i == size(t, 1))
        pos = [x(i, 3), x(i, 5)];
        alpha = x(i, 1);
        
        r = [cos(alpha), -sin(alpha);
             sin(alpha), cos(alpha)];
        
        edges = [ 0.1, -0.1, 0.1, -0.1;
                  1, 1, -1, -1]*50;
              
        for j=1:4
            edges(:, j) = r*edges(:,j);
        end
        for j=1:4
            for k=j+1:4
                plot(pos(1) + edges(1, [j,k]), pos(2) + edges(2, [j,k]), 'k')
            end
        end
    end
end

axis equal