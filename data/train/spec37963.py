import numpy as np 

def function(x):

	s6 = x
	r9 = x
	paths = []
	try:
		if x >= 8:
			r9 = 1+r9
			s6 = s6+3
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if r9 < 9:
			s6 = 7-s6
			paths.append(3)
		else:
			r9 = x-6
			s6 = 3-s6
			r9 = r9/1
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