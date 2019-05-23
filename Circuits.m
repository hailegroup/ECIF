function Z = Circuits( parameters, freq, circuitVersion )
%CIRCUITS Master circuit function file
%   This function contains all of the fitting functions
%--- Inputs
%   parameters  - the input parameters of order unity
%   freq        - column vector of frequencies
%   c_version   - a string with the version of the fit to be used
%--- Outputs
%   Z           - N x 2 array of real and imaginary impedance

switch(circuitVersion)
    case{'R', 'r'}
        Z = Resistor(parameters, freq);
    case {'RL'}
        Z = RL(parameters, freq);
    case{'RRQ', 'rrq'}
        Z = RRQ(parameters, freq);
    case{'RRQRQ', 'rrqrq'}
        Z = RRQRQ(parameters, freq);
    case{'RRCRC', 'rrcrc'}
        Z = RRCRC(parameters, freq);
    case {'RRQRQRQ', 'rrqrqrq'}
        Z = RRQRQRQ(parameters, freq);
    case{'5'}
        Z = RobCircuit_5(parameters, freq);
    case{'6a'}
        Z = RobCircuit_6a(parameters, freq);
    case{'6b'}
        Z = RobCircuit_6b(parameters, freq);
    case{'7a'}
        Z = RobCircuit_7a(parameters, freq);
    case{'7b'}
        Z = RobCircuit_7b(parameters, freq);
    case{'7c'}
        Z = RobCircuit_7c(parameters, freq);
    case{'8'}
        Z = RobCircuit_8(parameters, freq);
    case{'maier2006'}
        Z = maier2006(parameters, freq);
    otherwise
        errstr = ['Version ' circuitVersion ' not recognized.'];
        error(errstr);
end

end

function Z = Resistor(params, freqs)
% Simple resistor

R = params(1);

Z = R .* ones(length(freqs), 1);

Z = [real(Z) imag(Z)];

end

function Z = RL(params, freqs)
% RL parallel circuit

R = params(1);
L = params(2);
w = 2 * pi * freqs;
Z = 1./(1/R + 1./(1i * w * L));

Z = [real(Z) imag(Z)];
end

function Z = RRQ(params, freqs)
% RobCircuit_RRQ Equivalent circuit for a microelectrode.
% p = [R Rs Y n];

R   = params(1);
Rs  = params(2);
Y   = params(3);
n   = params(4);
w   = 2*pi*freqs;

Z   = R + Rs ./ (1 + Y.*Rs.*(1i*w).^n);
Z   = [real(Z) imag(Z)];
end

function Z = RRQRQ(params, freqs)
% RobCircuit_RRQRQ Equivalent circuit for a microelectrode.
% Here Q = CPE
% p = [R0 R1 Y1 n1 R2 Y2 n2];

R0   = params(1);
R1   = params(2);
Y1   = params(3);
n1   = params(4);
R2   = params(5);
Y2   = params(6);
n2   = params(7);
w    = 2*pi*freqs;

Z   = R0 + R1 ./ (1 + Y1.*R1.*(1i*w).^n1) + R2 ./ (1 + Y2.*R2.*(1i*w).^n2);
Z   = [real(Z) imag(Z)];
end

function Z = RRQRQRQ(params, freqs)
% RobCircuit_RRQRQRQ Equivalent circuit for a microelectrode.
% Here Q = CPE
% p = [R0 R1 Y1 n1 R2 Y2 n2 R3 Y3 n3;

R0   = params(1);
R1   = params(2);
Y1   = params(3);
n1   = params(4);
R2   = params(5);
Y2   = params(6);
n2   = params(7);
R3   = params(8);
Y3   = params(9);
n3   = params(10);
w    = 2*pi*freqs;

Z   = R0 + R1 ./ (1 + Y1.*R1.*(1i*w).^n1) + R2 ./ (1 + Y2.*R2.*(1i*w).^n2) + ...
     R3 ./ (1 + Y3.*R3.*(1i*w).^n3);
 
Z   = [real(Z) imag(Z)];
end


function Z = RRCRC(params, freqs)
% RobCircuit_RRCRC Equivalent circuit for a microelectrode.
% p = [R0 R1 C1 R2 C2];

R0   = params(1);
R1   = params(2);
C1   = params(3);
R2   = params(4);
C2   = params(5);
i    = 1i;
w    = 2*pi*freqs;

Z   = R0 + R1 ./ (1 + R1.*C1.*i*w) + R2 ./ (1 + R2.*C2.*i*w);
Z   = [real(Z) imag(Z)];
end

function Z = RobCircuit_5(params, freqs)
% RobCircuit_5 Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Cion_s Cchem  R0]

Rion    = params(1);
Rion_s  = params(2);
Cion_s  = params(3);
Cchem   = params(4);
R0      = params(5);
i       = 1i;
w       = 2*pi*freqs;

Zion_s  = Rion_s ./ (1 + i*w*Rion_s*Cion_s);
a       = sqrt(i*w*Rion*Cchem);

Z = (Rion + Zion_s.*a.*coth(a)) ./ (Zion_s.*a.^2./Rion + a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = RobCircuit_6a(params, freqs)
% RobCircuit_6a Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Cion_s Cchem Ceon_p R0]

Rion    = params(1);
Rion_s  = params(2);
Cion_s  = params(3);
Cchem   = params(4);
Ceon_p  = params(5);
R0      = params(6);
i       = 1i;
w       = 2*pi*freqs;

Zion_s  = Rion_s ./ (1+i*w*Rion_s*Cion_s);
Zeon_p  = 1./(i*w*Ceon_p);
a       = sqrt(i*w*Rion*Cchem);

Z = (Rion.*Zeon_p + Zeon_p.*Zion_s.*a.*coth(a)) ./ ...
    (Rion + Zion_s.*a.^2.*Zeon_p/Rion + (Zion_s + Zeon_p).*a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = RobCircuit_6b(params, freqs)
% RobCircuit_6b Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Cion_s Cchem Rion_p R0]

Rion    = params(1);
Rion_s  = params(2);
Cion_s  = params(3);
Cchem   = params(4);
Rion_p  = params(5);
R0      = params(6);
i       = 1i;
w       = 2*pi*freqs;

Zion_s  = Rion_s ./ (1+i*w*Rion_s*Cion_s);
Zion_p  = Rion_p;
a       = sqrt(1i*w*Rion*Cchem);

Z = (Rion^2 + Zion_s.*Zion_p.*a.^2 + Rion.*(Zion_s + Zion_p).*a.*coth(a)) ./ ...
    (Zion_s.*a.^2 + Rion.*a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = RobCircuit_7a(params, freqs)
% RobCircuit_7a Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Cion_s Cchem Rion_p Cion_p R0]  

Rion    = params(1);
Rion_s  = params(2);
Cion_s  = params(3);
Cchem   = params(4);
Rion_p  = params(5);
Cion_p  = params(6);
R0      = params(7);
i       = 1i;
w       = 2*pi*freqs;

Zion_s  = Rion_s ./ (1+i*w*Rion_s*Cion_s);
Zion_p  = Rion_p ./ (1+i*w*Rion_p*Cion_p);
a       = sqrt(1i*w*Rion*Cchem);

Z = (Rion^2 + Zion_s.*Zion_p.*a.^2 + Rion.*(Zion_s + Zion_p).*a.*coth(a)) ./ ...
    (Zion_s.*a.^2 + Rion.*a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = RobCircuit_7b(params, freqs)
% RobCircuit_7b Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Cion_s Cchem Yeon_p neon_p R0]

Rion    = params(1);
Rion_s  = params(2);
Cion_s  = params(3);
Cchem   = params(4);
Yeon_p  = params(5);
neon_p  = params(6);
R0      = params(7);
i       = 1i;
w       = 2*pi*freqs;

Zion_s  = Rion_s ./ (1+i*w*Rion_s*Cion_s);
Zeon_p  = 1 ./ (Yeon_p.*(i*w).^neon_p);
a       = sqrt(i*w*Rion*Cchem);

Z = (Rion.*Zeon_p + Zeon_p.*Zion_s.*a.*coth(a)) ./ ...
    (Rion + Zion_s.*a.^2.*Zeon_p./Rion + (Zion_s + Zeon_p).*a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = RobCircuit_7c(params, freqs)
% RobCircuit_7c Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Yion_s nion_s Cchem Ceon_p R0]

Rion    = params(1);
Rion_s  = params(2);
Yion_s  = params(3);
nion_s  = params(4);
Cchem   = params(5);
Ceon_p  = params(6);
R0      = params(7);
i       = 1i;
w       = 2*pi*freqs;

Z_A = Rion_s ./ (1+Rion_s*Yion_s*(i*w).^nion_s);
Z_D = 1 ./ (i*w*Ceon_p);
a   = sqrt(i*w*Rion*Cchem);

Z = (Rion .* Z_D + Z_D .* Z_A .* a .* coth(a)) ./ ...
    (Rion + Z_A .* Z_D .* a.^2 / Rion + (Z_A + Z_D).*a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = RobCircuit_8(params, freqs)
% RobCircuit_8 Equivalent circuit for a microelectrode.
% p = [Rion Rion_s Cion_s Cchem Rion_p Cion_p Ceon_p R0]

Rion    = params(1);
Rion_s  = params(2);
Cion_s  = params(3);
Cchem   = params(4);
Rion_p  = params(5);
Cion_p  = params(6);
Ceon_p  = params(7);
R0      = params(8);
i       = 1i;
w       = 2*pi*freqs;

Zion_s  = Rion_s ./ (1+i*w*Rion_s*Cion_s);
Zion_p  = Rion_p ./ (1+i*w*Rion_p*Cion_p);
Zeon_p  = 1./(i*w*Ceon_p);
a       = sqrt(i*w*Rion*Cchem);

Z = (Rion^2.*Zeon_p + Zion_s.*Zion_p.*Zeon_p.*a.^2 + Rion.*Zeon_p.*(Zion_s + Zion_p).*a.*coth(a)) ./ ...
    (Rion^2 + Zion_s.*a.^2.*(Zion_p + Zeon_p) + (Zion_s + Zion_p + Zeon_p).*Rion.*a.*coth(a)) + R0;
Z = [real(Z) imag(Z)];
end

function Z = maier2006(params, freqs)
% Maier2006 Physical circuit adapted from Baumann et. al. SSI 177 (2006)
% p = ['R_{lyte}', 'R_{ion,int}', 'Q_{int}', 'n_{ion,int}', 'R_{ion,surf}',
% 'Q_{chem}', 'n_{ion, surf}']

R_lyte      = params(1);
R_ion_int   = params(2);
Q_ion_int   = params(3);
n_ion_int   = params(4);
R_ion_surf  = params(5);
Q_chem      = params(6);
n_chem      = params(7);

i           = 1i;
w           = 2*pi*freqs;

Z_Q_ion_int = (Q_ion_int * (i*w).^(n_ion_int)).^(-1);
Z_Q_chem    = (Q_chem * (i*w).^(n_chem)).^(-1);

Ztop = R_ion_int + (R_ion_surf .* Z_Q_chem)./(R_ion_surf + Z_Q_chem);

Z = R_lyte + 1./(Z_Q_ion_int.^(-1) + Ztop.^(-1));
Z = [real(Z) imag(Z)];
end
