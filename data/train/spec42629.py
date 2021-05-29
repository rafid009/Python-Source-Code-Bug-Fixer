import numpy as np 

def function(x):

	m1 = 6
	x8 = x
	x = 5
	paths = []
	try:
		if x >= 3:
			m1 = 2-5
			paths.append(1)
		else:
			x = x*x
			x8 = 9-x8
			paths.append(2)
		if x > 0:
			m1 = m1*x
			x8 = 0-x8
			m1 = 4+1
			paths.append(3)
		else:
			x8 = x/8
			m1 = x8/1
			x8 = x8+5
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))