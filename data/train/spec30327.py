import numpy as np 

def function(x):

	s2 = x
	k8 = 9
	paths = []
	try:
		if k8 <= 3:
			x = 4/x
			paths.append(1)
		else:
			k8 = k8/s2
			paths.append(2)
		if k8 >= 6:
			k8 = 0*k8
			paths.append(3)
		else:
			k8 = k8*5
			x = x+2
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		s2 = s2**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))