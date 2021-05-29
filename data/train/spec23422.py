import numpy as np 

def function(x):

	k3 = x
	s6 = 3
	paths = []
	try:
		if x > 2:
			s6 = s6-3
			s6 = s6-k3
			paths.append(1)
		else:
			k3 = k3/7
			s6 = x*s6
			x = k3*7
			paths.append(2)
		if x < 3:
			k3 = k3-9
			paths.append(3)
		else:
			s6 = s6/6
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))