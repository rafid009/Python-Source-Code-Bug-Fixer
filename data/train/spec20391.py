import numpy as np 

def function(x):

	s2 = 3
	k3 = x
	paths = []
	try:
		if s2 >= 8:
			s2 = 7-s2
			paths.append(1)
		else:
			x = 6-x
			s2 = x*s2
			k3 = k3-k3
			paths.append(2)
		if x <= 5:
			x = 5+6
			k3 = 4*k3
			k3 = k3-4
			paths.append(3)
		else:
			k3 = 7-k3
			x = x*4
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		s2 = k3**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))