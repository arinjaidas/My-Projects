function y = simulateARMA(c, phi, theta, nu, T, burnIn, seed)
% October 2026 reconstruction, not the original local 2024 script.
% Requires Statistics and Machine Learning Toolbox for trnd.
% Innovations are normalized to unit variance; nu must exceed 2.
validateattributes(c, {'numeric'}, {'scalar','real','finite'});
validateattributes(phi, {'numeric'}, {'scalar','real','finite','>',-1,'<',1});
validateattributes(theta, {'numeric'}, {'scalar','real','finite'});
validateattributes(nu, {'numeric'}, {'scalar','real','finite','>',2});
validateattributes(T, {'numeric'}, {'scalar','integer','>=',3});
validateattributes(burnIn, {'numeric'}, {'scalar','integer','>=',0});
rng(seed, 'twister');
epsilon = trnd(nu, T + burnIn + 1, 1) .* sqrt((nu - 2) / nu);
values = zeros(T + burnIn, 1);
last = c / (1 - phi);
for t = 2:(T + burnIn + 1)
    last = c + phi * last + epsilon(t) + theta * epsilon(t - 1);
    values(t - 1) = last;
end
y = values((burnIn + 1):end);
end
