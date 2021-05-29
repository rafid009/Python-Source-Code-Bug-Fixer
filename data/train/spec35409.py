import numpy as np 

def function(x):

	s9 = x
	x0 = x
	paths = []
	try:
		if x0 > 3:
			x = 8+x
			x = x/4
			x0 = 5+x0
			paths.append(1)
		else:
			s9 = s9*6
			paths.append(2)
		if s9 >= 8:
			x0 = x0+2
			paths.append(3)
		else:
			x = x0*x
			x = x+s9
			x0 = 2-x0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x0 = s9**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))