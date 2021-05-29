import numpy as np 

def function(x):

	y5 = x
	m3 = 6
	paths = []
	try:
		if y5 < 5:
			y5 = y5+3
			paths.append(1)
		else:
			m3 = 9+m3
			y5 = y5/y5
			x = x-1
			paths.append(2)
		if x >= 7:
			x = y5-1
			paths.append(3)
		else:
			m3 = 4/m3
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		x = y5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))