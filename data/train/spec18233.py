import numpy as np 

def function(x):

	z2 = 1
	m4 = 7
	paths = []
	try:
		if x <= 1:
			z2 = 0+9
			z2 = z2+8
			z2 = 4*8
			paths.append(1)
		else:
			z2 = z2/7
			z2 = z2/3
			paths.append(2)
		if z2 < 8:
			m4 = 8+6
			x = m4+x
			m4 = m4-4
			paths.append(3)
		else:
			m4 = m4-8
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))