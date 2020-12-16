def covariance_spin( spins, r ) :
  # Your code goes here
  avspin, corr = sum(spins)/len(spins), 0 
  for i in range(len(spins)) : corr = corr + (spins[i]-avspin)*(spins[(i+r)%len(spins)]-avspin)
  return corr / len(spins)

spins1 = [1,-1,1,1,-1,1,1,1,-1,-1]
print( covariance_spin( spins1, 1 ), covariance_spin( spins1, 2 ), covariance_spin( spins1, 3 ) )
spins2 = [-1,1,1,1,-1,-1,1,1,1,-1]
print( covariance_spin( spins2, 2 ), covariance_spin( spins2, 2 ), covariance_spin( spins2, 3 ) )
