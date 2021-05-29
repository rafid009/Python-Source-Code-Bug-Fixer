import numpy as np 

def function(x):

	z1 = 9
	m7 = x
	paths = []
	try:
		if z1 > 3:
			z1 = x-9
			x = m7+m7
			paths.append(1)
		else:
			m7 = x/z1
			m7 = m7/9
			paths.append(2)
		if m7 >= 4:
			m7 = 2/z1
			x = z1*x
			x = 6-1
			paths.append(3)
		else:
			m7 = m7/8
			z1 = x/m7
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m7 = x**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))