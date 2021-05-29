import numpy as np 

def function(x):

	m0 = x
	z8 = x
	paths = []
	try:
		if x >= 7:
			x = m0/x
			m0 = z8+m0
			x = x-8
			paths.append(1)
		else:
			m0 = m0*1
			z8 = z8/x
			m0 = 2+x
			paths.append(2)
		if m0 <= 6:
			z8 = z8*4
			z8 = z8-m0
			paths.append(3)
		else:
			m0 = m0*0
			z8 = m0+z8
			z8 = z8-m0
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		m0 = z8**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))