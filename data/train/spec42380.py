import numpy as np 

def function(x):

	s7 = x
	f5 = x
	paths = []
	try:
		if x > 8:
			x = 5+x
			paths.append(1)
		else:
			s7 = s7+4
			f5 = 6+f5
			x = 6/s7
			paths.append(2)
		if f5 > 2:
			x = 2-x
			paths.append(3)
		else:
			f5 = f5+2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))