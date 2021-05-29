import numpy as np 

def function(x):

	z5 = x
	m4 = 6
	paths = []
	try:
		if x <= 8:
			z5 = m4/z5
			x = x/9
			z5 = z5+x
			paths.append(1)
		else:
			x = x*z5
			x = x-6
			x = 2-7
			paths.append(2)
		if m4 >= 4:
			x = z5-3
			paths.append(3)
		else:
			m4 = m4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))