import numpy as np 

def function(x):

	p7 = 6
	s9 = 7
	paths = []
	try:
		if x < 5:
			p7 = 2/p7
			p7 = p7/3
			paths.append(1)
		else:
			s9 = x+p7
			paths.append(2)
		if s9 >= 5:
			s9 = s9-9
			x = x*x
			x = s9*x
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))