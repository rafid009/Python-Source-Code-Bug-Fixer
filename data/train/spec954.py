import numpy as np 

def function(x):

	s5 = x
	v5 = x
	paths = []
	try:
		if s5 <= 8:
			s5 = 6/s5
			paths.append(1)
		else:
			x = x-1
			paths.append(2)
		if x > 5:
			s5 = s5-s5
			paths.append(3)
		else:
			s5 = 7+v5
			v5 = 3/s5
			x = x/2
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