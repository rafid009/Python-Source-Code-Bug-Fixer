import numpy as np 

def function(x):

	m3 = 4
	z2 = 4
	paths = []
	try:
		if m3 < 4:
			x = x-x
			z2 = z2*2
			paths.append(1)
		else:
			m3 = m3-4
			x = x+8
			paths.append(2)
		if z2 > 0:
			m3 = 7+m3
			paths.append(3)
		else:
			x = m3-x
			m3 = m3*8
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