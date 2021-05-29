import numpy as np 

def function(x):

	u9 = x
	s8 = 8
	paths = []
	try:
		if x <= 7:
			s8 = u9/x
			x = x/8
			paths.append(1)
		else:
			x = u9/x
			paths.append(2)
		if s8 > 9:
			u9 = u9/u9
			x = 7/x
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		x = u9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))