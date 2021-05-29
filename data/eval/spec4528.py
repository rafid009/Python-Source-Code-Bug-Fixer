import numpy as np 

def function(x):

	s5 = x
	z4 = 7
	paths = []
	try:
		if x >= 4:
			s5 = s5*1
			s5 = x+s5
			x = 5*1
			paths.append(1)
		else:
			z4 = z4+4
			z4 = z4*x
			paths.append(2)
		if x <= 9:
			s5 = 9-6
			paths.append(3)
		else:
			z4 = z4+s5
			x = x*8
			z4 = 0+8
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