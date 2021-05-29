import numpy as np 

def function(x):

	z1 = x
	m3 = 8
	paths = []
	try:
		if x < 2:
			x = 3-z1
			m3 = z1-z1
			x = x*6
			paths.append(1)
		else:
			m3 = m3-x
			m3 = m3/m3
			m3 = m3-m3
			paths.append(2)
		if z1 <= 5:
			z1 = 3+z1
			x = 2*m3
			paths.append(3)
		else:
			z1 = z1-2
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))