import numpy as np 

def function(x):

	s4 = x
	k8 = x
	paths = []
	try:
		if s4 <= 4:
			k8 = 2*k8
			s4 = s4+x
			paths.append(1)
		else:
			k8 = x+3
			k8 = 1-k8
			paths.append(2)
		if s4 > 0:
			k8 = k8+4
			s4 = 4*8
			paths.append(3)
		else:
			x = x+4
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k8 = x**0.5
		return k8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))