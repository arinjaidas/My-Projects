% Reconstructed December 2024 parameter setting. Not executed for this release.
c = 2; phi = 0.95; theta = 0.25; nu = 4; T = 800; burnIn = 50;
y = simulateARMA(c, phi, theta, nu, T, burnIn, 20261019);
theoreticalMean = c / (1 - phi);
theoreticalVariance = (1 + theta^2 + 2*phi*theta) / (1 - phi^2);
fprintf('Theoretical mean %.6f, variance %.6f\n', theoreticalMean, theoreticalVariance);
fprintf('Sample mean %.6f, variance %.6f\n', mean(y), var(y));
writetable(table((1:T)', y, 'VariableNames', {'t','synthetic_y'}), 'arma_sample.csv');
figure; plot(y); yline(theoreticalMean, '--');
title('Synthetic ARMA(1,1), unit-variance Student-t innovations');
xlabel('Observation'); ylabel('Simulated level'); grid on;
