import numpy as np 

def function(x):

	s4 = x
	b3 = 7
	paths = []
	try:
		if x < 9:
			s4 = s4-6
			x = 5/1
			paths.append(1)
		else:
			b3 = s4+b3
			paths.append(2)
		if s4 < 9:
			x = 6/x
			paths.append(3)
		else:
			x = 2*3
			b3 = 3*b3
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