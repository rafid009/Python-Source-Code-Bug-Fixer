import numpy as np 

def function(x):

	k8 = 9
	s4 = 7
	paths = []
	try:
		if x > 9:
			x = 8+x
			paths.append(1)
		else:
			s4 = s4-9
			s4 = s4-3
			x = 3+x
			paths.append(2)
		if k8 <= 9:
			x = 1/x
			paths.append(3)
		else:
			k8 = k8+0
			x = x-k8
			x = 1+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))