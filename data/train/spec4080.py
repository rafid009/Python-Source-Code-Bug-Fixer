import numpy as np 

def function(x):

	s2 = x
	w9 = 9
	x = 5
	paths = []
	try:
		if w9 >= 5:
			w9 = w9+4
			x = 4/w9
			x = 6*7
			paths.append(1)
		else:
			x = x-5
			w9 = w9+w9
			s2 = s2-5
			paths.append(2)
		if x > 1:
			x = 4-x
			s2 = s2+3
			paths.append(3)
		else:
			s2 = s2+4
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))