import numpy as np 

def function(x):

	v1 = x
	s6 = x
	paths = []
	try:
		if v1 < 1:
			v1 = x*v1
			paths.append(1)
		else:
			s6 = s6*6
			x = x/2
			paths.append(2)
		if x > 0:
			v1 = 0/7
			paths.append(3)
		else:
			v1 = 6*v1
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))