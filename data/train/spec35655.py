import numpy as np 

def function(x):

	z1 = x
	m2 = 4
	paths = []
	try:
		if z1 <= 3:
			x = 7+x
			z1 = z1*6
			paths.append(1)
		else:
			z1 = z1+9
			paths.append(2)
		if m2 >= 7:
			x = x-2
			x = x*8
			z1 = 7*m2
			paths.append(3)
		else:
			z1 = z1*6
			x = x*8
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))