#Prediction-Sim (Agent-based Model)

This simulation explores the distributional wealth impacts of various
betting strategies in a prediction market with contracts set on the 
open interval (0,1). Inputs may be predefined or randomly assigned. Agents are
vested with "beliefs" and may or may not update these when presented with new 
information. Derivative events are artificially generated using one or a 
combination of Lévy processes including: Brownian Motion, Laplace motion, 
and/or extensions of these to the Black-Scholes model for futures. Due 
to difficulties enforcing boundary conditions, all trading is restricted when 
market prices exceed these limits. Trading occurs asyncronously, though 
modification to allow syncronous or other ordered trades should be trivial..
