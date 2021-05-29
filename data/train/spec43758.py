import numpy as np 

def function(x):

	m4 = x
	a8 = x
	paths = []
	try:
		if a8 > 7:
			m4 = 4*a8
			paths.append(1)
		else:
			x = a8*x
			paths.append(2)
		if a8 > 9:
			a8 = 5*4
			m4 = m4-5
			a8 = a8*a8
			paths.append(3)
		else:
			x = x+m4
			a8 = a8+9
			a8 = 6*2
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