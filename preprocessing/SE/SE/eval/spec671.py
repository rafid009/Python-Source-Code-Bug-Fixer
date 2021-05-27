import numpy as np 

def function(x):

	y4 = 8
	m9 = 5
	paths = []
	try:
		if x < 6:
			m9 = 4/y4
			m9 = m9*5
			m9 = 9+m9
			paths.append(1)
		else:
			m9 = 9-x
			x = m9+2
			x = x+8
			paths.append(2)
		if x <= 7:
			y4 = 1+4
			y4 = 5-y4
			paths.append(3)
		else:
			x = x*2
			y4 = 1/m9
			x = 6/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))