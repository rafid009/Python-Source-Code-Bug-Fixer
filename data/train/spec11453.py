import numpy as np 

def function(x):

	s2 = x
	r9 = 4
	paths = []
	try:
		if x <= 6:
			r9 = 8/3
			paths.append(1)
		else:
			r9 = r9-3
			x = x*4
			s2 = 1+s2
			paths.append(2)
		if s2 > 4:
			s2 = s2*x
			x = 2/5
			paths.append(3)
		else:
			r9 = r9+r9
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