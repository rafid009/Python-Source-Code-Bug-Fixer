import numpy as np 

def function(x):

	z6 = 0
	m8 = x
	paths = []
	try:
		if m8 < 8:
			z6 = z6*9
			paths.append(1)
		else:
			z6 = 0+x
			paths.append(2)
		if m8 < 3:
			x = 4+x
			x = 8*0
			paths.append(3)
		else:
			m8 = m8*x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))