import numpy as np 

def function(x):

	m4 = 7
	e5 = x
	x = x
	paths = []
	try:
		if m4 > 3:
			m4 = e5*2
			x = x*7
			paths.append(1)
		else:
			m4 = m4*8
			x = 9*x
			paths.append(2)
		if m4 < 3:
			x = 9-x
			e5 = 7*e5
			x = e5/e5
			paths.append(3)
		else:
			m4 = m4-x
			e5 = 2-2
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))