import numpy as np 

def function(x):

	f8 = 8
	s4 = x
	paths = []
	try:
		if s4 > 8:
			x = x/f8
			paths.append(1)
		else:
			x = f8*2
			paths.append(2)
		if x > 3:
			f8 = f8/2
			paths.append(3)
		else:
			s4 = s4/s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		x = s4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))