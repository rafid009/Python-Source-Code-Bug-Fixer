import numpy as np 

def function(x):

	k3 = x
	s6 = 6
	x = x
	paths = []
	try:
		if k3 >= 4:
			s6 = 5-8
			x = x*1
			paths.append(1)
		else:
			x = 4*6
			paths.append(2)
		if k3 < 0:
			s6 = s6*4
			s6 = 7/s6
			s6 = s6-x
			paths.append(3)
		else:
			x = 9+x
			s6 = 7-s6
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))