import numpy as np 

def function(x):

	k3 = 7
	s0 = x
	paths = []
	try:
		if k3 < 9:
			x = x-0
			k3 = k3-5
			s0 = s0/s0
			paths.append(1)
		else:
			x = s0-5
			s0 = s0/3
			paths.append(2)
		if s0 > 3:
			s0 = s0/k3
			x = s0+3
			paths.append(3)
		else:
			k3 = k3+1
			k3 = k3-8
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