import numpy as np 

def function(x):

	m1 = x
	d8 = x
	paths = []
	try:
		if d8 >= 2:
			x = 1+7
			m1 = x+7
			paths.append(1)
		else:
			d8 = d8*3
			x = 6/3
			x = x-2
			paths.append(2)
		if x <= 1:
			x = x+9
			x = m1*x
			x = 9+x
			paths.append(3)
		else:
			m1 = m1+6
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))