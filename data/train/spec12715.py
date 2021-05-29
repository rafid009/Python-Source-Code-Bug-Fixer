import numpy as np 

def function(x):

	g2 = 1
	m9 = x
	x = 1
	paths = []
	try:
		if m9 >= 4:
			x = x-5
			x = x+1
			paths.append(1)
		else:
			x = 4*g2
			paths.append(2)
		if x > 3:
			x = m9-2
			x = 5-x
			g2 = g2*9
			paths.append(3)
		else:
			m9 = 5-g2
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