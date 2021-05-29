import numpy as np 

def function(x):

	x9 = 1
	s6 = 5
	paths = []
	try:
		if x <= 1:
			x = x/5
			paths.append(1)
		else:
			x9 = x9*x
			x9 = x+x9
			paths.append(2)
		if x9 > 4:
			x9 = x9+0
			paths.append(3)
		else:
			x9 = x9-9
			s6 = x+s6
			x9 = x/x9
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))