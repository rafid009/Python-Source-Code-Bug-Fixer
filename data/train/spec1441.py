import numpy as np 

def function(x):

	z2 = 3
	m7 = 1
	paths = []
	try:
		if z2 < 5:
			m7 = m7+6
			paths.append(1)
		else:
			x = m7*m7
			paths.append(2)
		if m7 < 1:
			m7 = 6+0
			z2 = z2/z2
			paths.append(3)
		else:
			z2 = z2/6
			m7 = x+z2
			x = x/5
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		z2 = m7**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))