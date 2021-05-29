import numpy as np 

def function(x):

	s7 = 7
	r6 = 3
	paths = []
	try:
		if x >= 0:
			x = x*x
			s7 = 4-s7
			paths.append(1)
		else:
			x = r6/x
			paths.append(2)
		if s7 > 9:
			s7 = s7-r6
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		r6 = s7**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))