import numpy as np 

def function(x):

	s6 = x
	k6 = 8
	paths = []
	try:
		if k6 < 2:
			k6 = k6/3
			k6 = k6*4
			paths.append(1)
		else:
			s6 = 8-s6
			x = x*s6
			paths.append(2)
		if x > 8:
			k6 = k6*5
			paths.append(3)
		else:
			k6 = s6*2
			x = x+2
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k6 = x**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))