import numpy as np 

def function(x):

	e7 = 5
	m1 = x
	x = x
	paths = []
	try:
		if m1 >= 1:
			x = 2-x
			x = x/3
			paths.append(1)
		else:
			m1 = 3/m1
			m1 = 7+1
			m1 = 6/5
			paths.append(2)
		if m1 > 9:
			x = 3-6
			paths.append(3)
		else:
			m1 = 2*1
			x = x/7
			e7 = e7/m1
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