import numpy as np 

def function(x):

	f8 = x
	s7 = x
	paths = []
	try:
		if x >= 8:
			s7 = f8*s7
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if s7 > 7:
			x = x-3
			x = x-3
			x = x-s7
			paths.append(3)
		else:
			s7 = s7/2
			x = x-5
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		f8 = s7**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))