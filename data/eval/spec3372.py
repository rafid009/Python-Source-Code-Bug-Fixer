import numpy as np 

def function(x):

	m3 = x
	z1 = 4
	paths = []
	try:
		if m3 <= 6:
			z1 = m3+9
			x = z1+2
			z1 = z1*1
			paths.append(1)
		else:
			z1 = m3/1
			z1 = m3/x
			paths.append(2)
		if z1 < 2:
			x = x+4
			paths.append(3)
		else:
			z1 = m3+4
			x = m3/7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m3 = x**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))