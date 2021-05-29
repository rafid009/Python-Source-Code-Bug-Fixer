import numpy as np 

def function(x):

	s5 = x
	z2 = 4
	x = 0
	paths = []
	try:
		if z2 >= 1:
			z2 = 2/z2
			x = x+2
			paths.append(1)
		else:
			s5 = 3+s5
			x = 9-4
			s5 = 7*5
			paths.append(2)
		if z2 > 8:
			s5 = s5*2
			s5 = 7+0
			paths.append(3)
		else:
			x = z2+s5
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