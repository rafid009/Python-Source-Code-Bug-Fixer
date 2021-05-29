import numpy as np 

def function(x):

	s4 = x
	x1 = x
	paths = []
	try:
		if x1 > 9:
			s4 = s4-2
			x1 = s4-x1
			x = x/3
			paths.append(1)
		else:
			x1 = x1/9
			s4 = 9/9
			paths.append(2)
		if s4 > 7:
			x = 2-x
			x = 0/x
			paths.append(3)
		else:
			x = s4/2
			s4 = s4/6
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))