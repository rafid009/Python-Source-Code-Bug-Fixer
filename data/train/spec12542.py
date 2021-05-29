import numpy as np 

def function(x):

	s5 = 9
	o3 = x
	paths = []
	try:
		if o3 >= 3:
			s5 = 7-9
			s5 = 1*s5
			paths.append(1)
		else:
			s5 = 2-s5
			paths.append(2)
		if s5 > 8:
			o3 = s5+3
			x = 7/x
			paths.append(3)
		else:
			s5 = 0+x
			o3 = o3+x
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