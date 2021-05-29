import numpy as np 

def function(x):

	z2 = x
	m5 = 6
	paths = []
	try:
		if z2 <= 1:
			z2 = 9/z2
			paths.append(1)
		else:
			x = m5-x
			m5 = m5/3
			paths.append(2)
		if m5 > 7:
			x = m5+4
			paths.append(3)
		else:
			z2 = 0+z2
			x = z2+6
			z2 = z2/4
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))