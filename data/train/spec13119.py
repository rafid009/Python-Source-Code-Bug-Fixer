import numpy as np 

def function(x):

	m1 = 7
	y4 = x
	paths = []
	try:
		if m1 > 5:
			y4 = y4/9
			m1 = 1/x
			m1 = m1*y4
			paths.append(1)
		else:
			x = x*y4
			x = y4+6
			paths.append(2)
		if x > 3:
			x = 0*x
			x = x*3
			paths.append(3)
		else:
			y4 = 1+y4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))