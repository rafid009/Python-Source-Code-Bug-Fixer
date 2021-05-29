import numpy as np 

def function(x):

	a8 = x
	m3 = x
	paths = []
	try:
		if m3 > 5:
			a8 = 3/a8
			x = x*m3
			paths.append(1)
		else:
			m3 = 3*5
			x = 9*a8
			paths.append(2)
		if x > 5:
			x = 2/x
			x = x+0
			paths.append(3)
		else:
			m3 = 5/m3
			m3 = 0*m3
			a8 = a8*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))