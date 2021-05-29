import numpy as np 

def function(x):

	v5 = x
	s8 = 6
	paths = []
	try:
		if x < 8:
			s8 = s8*8
			paths.append(1)
		else:
			x = x/9
			paths.append(2)
		if x >= 2:
			s8 = s8/2
			v5 = 1/s8
			paths.append(3)
		else:
			x = 5/x
			x = 0/x
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		x = v5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))