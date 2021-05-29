import numpy as np 

def function(x):

	z6 = x
	m7 = x
	paths = []
	try:
		if x > 8:
			m7 = m7*5
			x = x/6
			paths.append(1)
		else:
			z6 = z6+1
			z6 = z6*4
			paths.append(2)
		if m7 < 8:
			x = 9*8
			m7 = m7-x
			paths.append(3)
		else:
			x = m7*x
			z6 = z6/9
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		z6 = m7**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))