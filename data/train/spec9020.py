import numpy as np 

def function(x):

	z7 = x
	m9 = x
	paths = []
	try:
		if m9 > 9:
			x = x+m9
			x = x/1
			z7 = 2+z7
			paths.append(1)
		else:
			z7 = 5-m9
			paths.append(2)
		if z7 > 3:
			m9 = z7/9
			x = 0+x
			paths.append(3)
		else:
			x = x+z7
			m9 = 3-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))