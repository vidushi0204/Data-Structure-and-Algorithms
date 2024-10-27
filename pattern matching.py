import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)



#------------------------------------------findN------------------------------------------
# return appropriate N that satisfies the error bounds
def findN(eps,m):
	N=4
	while(N/math.log2(N))<=2*math.log2(26)*(m/eps):
		N*=4
	N=N//2
	if((N/math.log2(N))<=2*math.log2(26)*(m/eps)):
		return N*2
	else:
		return N
"""
Number to find: N
Suppose s1 and s2 are 2 strings of same length. Let q be a prime number.
False postive happens when f(a)!=f(b) but f(a) mod q== f(b) mod q
==>q must divide f(a)-f(b) for false outcome
q<N(given)
Probablity of false outcome P = number of prime factors of (f(a)-f(b))/(Number of prime nos less than N)
CLAIM 1:
Number of prime factors of some positive integer x is atmost log2(x)
CLAIM 2:
Let π(N) denote the number of prime nos less than or equal to N. 
For all N > 1, π(N) ≥ N/(2*log2(N))

Maximum possible value of f(a)-f(b)=26^m-1
P<log2(26^m)/(N/(2*log2(N)))<eps
Hence, N/log2(N)>2*log2(26)*(m/eps)
"""


#------------------------------------------modPatternMatch------------------------------------------
# Return sorted list of starting indices where p matches x
#TC- Time Complexity
#SC- Space Complexity
def modPatternMatch(q,p,x):
	m=len(p)		#TC:O(1), SC:O(log2(m))
	n=len(x)		#TC:O(1), SC:O(log2(n))
	sum=ord(x[0])-65	# Stores hash value of substrings of x(of length m)[given by function f(y)]
	psum=ord(p[0])-65	# Stores hash value of p
	L=[]			#OUTPUT LIST
	pwr=1	

	"""[Multiplication operation with x mod q [x is a number] => involves log2(q) bits at max --> TC:O(log2(q))]"""

	for i in range(m):
		pwr*=26
		pwr=pwr%q
	#TC:O(m.log2(q)), SC:O(log2(q))
		
	
	for i in range(1,m):
		sum=(sum*26+ord(x[i])-65)%q		#Hash value of substring x[0:m]		
		psum=(psum*26+ord(p[i])-65)%q	#Hash value of p				
	#TC:O(m.log2(q)), SC:O(log2(q)) 	

	if(sum==psum):
		L.append(0)

	
	for i in range(0,n-m):
		sum=((sum*26+ord(x[i+m])-65)%q-(pwr*(ord(x[i])-65))%q+q)%q	
		#hash[i+1:i+m+1]=hash[i:i+m]*26 - number(x[i])*26^m + number(x[i+m]) --> Take mod q

		if(sum==psum):
			L.append(i+1)
	#TC:O((n-m).log2(q)), SC: O(k)+O(log2(q))	
	return L

"""
OVERALL TIME COMPLEXITY = O(m.log2(q)) + O((n-m).log2(q)) = O((m+n).log2(q))
m>n (observation) => OVERALL TC = O(n.log2(q)) which is the required TIME COMPLEXITY

OVERALL SPACE COMPLEXITY = O(log2(m)) + O(log2(n)) + O(log2(q)) + O(k)
m>n (observation) => OVERALL SC = O(log2(m)+log2(q)+k)
"""


#------------------------------------------modPatternMatchWildcard------------------------------------------
# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
	m=len(p)		#TC:O(1), SC:O(log2(m))
	n=len(x)		#TC:O(1), SC:O(log2(n))
	sum=ord(x[0])-65		# Stores hash value of substrings of x(of length m)[given by function f(y)]
	psum=ord(p[0])-65		# Stores hash value of substrings of p

	L=[]					#OUTPUT LIST
	
	"""[Multiplication operation with x mod q [x is a number] => involves log2(q) bits at max --> TC:O(log2(q))]"""

	pwr=1
	#Returns 26 raised to the power m(mod q) 
	for i in range(m):
		pwr*=26
		pwr=pwr%q
	#TC:O(m.log2(q)), SC:O(log2(q))

	
	for i in range(m):
		if(p[i]=='?'):
			ind=i		#Stores the index in p where '?' has been placed
			break

	ekpwr=1	
	#Returns 26 raised to the power m-1-ind (mod q) 
	for i in range(m-1-ind):
		ekpwr*=26
		ekpwr=ekpwr%q
	#TC:O((m-ind).log2(q)), SC:O(log2(q))
	

	for i in range(1,m):
		sum=(sum*26+ord(x[i])-65)%q		#Hash value of substring x[0:m]
		#Hash value of substring p(numeric value of ? is taken 0)
		if(p[i]!='?'):
			psum=(psum*26+ord(p[i])-65)%q
		else:
			psum=(psum*26)%q
		#TC:O(m.log2(q)), SC:O(log2(q)) 	

	store=(sum-(ekpwr*((ord(x[ind])-65)))%q+q)%q	#Stores hash value of subtrings of x(of length m)[with index<ind> replaced with '?']

	if(store==psum):
		L.append(0)

	for i in range(0,n-m):
		sum=((sum*26+ord(x[i+m])-65)%q-(pwr*(ord(x[i])-65))%q+q)%q
		#hash[i+1:i+m+1]=hash[i:i+m]*26 - number(x[i])*26^m + number(x[i+m]) --> Take mod q

		store=(sum-(ekpwr*((ord(x[i+ind+1]))-65))%q+q)%q #Hash value of x[i+1:i+m+1] if i+ind^th+1 index was replaced with '?'
		
		if(store==psum):
			L.append(i+1)
	#TC:O((n-m).log2(q)), SC: O(k)+O(log2(q))

	return L
"""
OVERALL TIME COMPLEXITY = O(m.log2(q)) + O((n-m).log2(q)) = O((m+n).log2(q))
m>n (observation) => OVERALL TC = O(n.log2(q)) which is the required TIME COMPLEXITY

OVERALL SPACE COMPLEXITY = O(log2(m)) + O(log2(n)) + O(log2(q)) + O(k)
m>n (observation) => OVERALL SC = O(log2(m)+log2(q)+k)
"""

