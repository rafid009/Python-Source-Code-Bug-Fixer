import numpy as np 

def function(x):

	s8 = 2
	k5 = 3
	paths = []
	try:
		if k5 <= 2:
			k5 = k5*2
			x = s8/x
			paths.append(1)
		else:
			s8 = s8+s8
			paths.append(2)
		if s8 >= 7:
			k5 = k5-x
			k5 = s8*k5
			k5 = x/k5
			paths.append(3)
		else:
			k5 = 4*1
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