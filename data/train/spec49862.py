import numpy as np 

def function(x):

	k7 = x
	s6 = x
	paths = []
	try:
		if x <= 7:
			k7 = 0-k7
			s6 = 4/k7
			s6 = s6*7
			paths.append(1)
		else:
			x = 1/1
			x = x/2
			paths.append(2)
		if s6 <= 4:
			k7 = 3-k7
			x = x/x
			paths.append(3)
		else:
			s6 = 1*k7
			k7 = k7/k7
			s6 = x*0
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))