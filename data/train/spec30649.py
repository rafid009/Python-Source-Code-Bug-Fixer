import numpy as np 

def function(x):

	s2 = 3
	k3 = 1
	paths = []
	try:
		if s2 >= 0:
			x = k3/x
			x = 2-9
			paths.append(1)
		else:
			s2 = s2+1
			paths.append(2)
		if s2 >= 2:
			s2 = k3+k3
			paths.append(3)
		else:
			s2 = 8*3
			s2 = 0*s2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k3 = x**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))