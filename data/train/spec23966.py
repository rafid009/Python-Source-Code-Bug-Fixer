import numpy as np 

def function(x):

	m3 = 7
	y8 = x
	paths = []
	try:
		if x < 7:
			m3 = x+m3
			paths.append(1)
		else:
			y8 = y8*y8
			m3 = x*5
			m3 = 5+m3
			paths.append(2)
		if x >= 3:
			m3 = x-5
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))