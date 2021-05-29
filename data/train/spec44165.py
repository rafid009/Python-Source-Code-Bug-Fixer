import numpy as np 

def function(x):

	z1 = x
	m5 = x
	paths = []
	try:
		if z1 >= 8:
			z1 = 7/4
			z1 = 6*z1
			paths.append(1)
		else:
			z1 = 4/3
			m5 = m5/5
			x = 2/x
			paths.append(2)
		if m5 <= 3:
			z1 = z1+0
			paths.append(3)
		else:
			m5 = x*m5
			z1 = z1/m5
			m5 = z1+m5
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