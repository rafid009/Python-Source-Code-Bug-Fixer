import numpy as np 

def function(x):

	d7 = x
	m7 = 2
	paths = []
	try:
		if x >= 4:
			x = 0+x
			x = x*x
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if d7 >= 2:
			x = x/x
			x = 9-7
			paths.append(3)
		else:
			m7 = x*x
			x = 5+9
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))