import numpy as np 

def function(x):

	z1 = 0
	m7 = 7
	paths = []
	try:
		if m7 <= 3:
			m7 = m7/9
			paths.append(1)
		else:
			m7 = 5+5
			m7 = 8/m7
			paths.append(2)
		if x < 4:
			m7 = z1/8
			m7 = m7-3
			paths.append(3)
		else:
			x = x+9
			z1 = 5+z1
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