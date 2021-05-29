import numpy as np 

def function(x):

	s9 = 0
	u8 = x
	paths = []
	try:
		if x > 6:
			s9 = 9-2
			paths.append(1)
		else:
			x = s9*x
			paths.append(2)
		if x < 5:
			x = 1-3
			x = s9/x
			paths.append(3)
		else:
			x = x/u8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))