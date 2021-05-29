import numpy as np 

def function(x):

	y4 = 8
	m2 = x
	paths = []
	try:
		if x > 6:
			m2 = y4+6
			x = 4/8
			x = m2*x
			paths.append(1)
		else:
			y4 = 9+y4
			x = 5/x
			y4 = 2-4
			paths.append(2)
		if x <= 8:
			x = 4+x
			m2 = 7+4
			x = x/4
			paths.append(3)
		else:
			x = x+5
			x = m2/x
			m2 = m2+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))