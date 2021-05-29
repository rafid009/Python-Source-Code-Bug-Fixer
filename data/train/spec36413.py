import numpy as np 

def function(x):

	d5 = x
	m1 = 1
	paths = []
	try:
		if x < 5:
			x = 8/9
			paths.append(1)
		else:
			m1 = 6*3
			paths.append(2)
		if x <= 1:
			d5 = d5*x
			paths.append(3)
		else:
			x = 3/x
			x = 1-4
			m1 = m1+2
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))