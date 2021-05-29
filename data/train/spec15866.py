import numpy as np 

def function(x):

	w9 = x
	s6 = x
	x = x
	paths = []
	try:
		if x > 5:
			s6 = 1-s6
			paths.append(1)
		else:
			x = w9*3
			s6 = s6+7
			paths.append(2)
		if s6 <= 0:
			x = 8*s6
			x = 6+x
			x = x*6
			paths.append(3)
		else:
			s6 = s6+8
			x = 8/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w9 = x**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))