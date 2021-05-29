import numpy as np 

def function(x):

	m3 = x
	d7 = 0
	paths = []
	try:
		if m3 < 8:
			x = 8/6
			paths.append(1)
		else:
			x = x/x
			d7 = d7/m3
			paths.append(2)
		if x < 6:
			d7 = d7*d7
			paths.append(3)
		else:
			x = 7*6
			x = x+6
			d7 = 7*d7
			paths.append(4)
		paths.append(5)
		assert m3 >= 0
		x = m3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))