import numpy as np 

def function(x):

	s2 = x
	k5 = x
	paths = []
	try:
		if s2 <= 0:
			s2 = x/4
			paths.append(1)
		else:
			x = x-x
			x = x+5
			paths.append(2)
		if s2 >= 8:
			k5 = 9*2
			k5 = k5/k5
			paths.append(3)
		else:
			s2 = s2-8
			k5 = 2-k5
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))