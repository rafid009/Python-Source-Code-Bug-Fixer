import numpy as np 

def function(x):

	s7 = x
	z1 = x
	x = 5
	paths = []
	try:
		if s7 < 3:
			s7 = 8/1
			s7 = s7-3
			x = 1/z1
			paths.append(1)
		else:
			z1 = s7*9
			s7 = z1*s7
			x = x+6
			paths.append(2)
		if x > 9:
			s7 = 2/4
			x = 8/4
			s7 = x*s7
			paths.append(3)
		else:
			x = x-x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))