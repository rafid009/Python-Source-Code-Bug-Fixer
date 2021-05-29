import numpy as np 

def function(x):

	m1 = x
	e0 = 7
	paths = []
	try:
		if x > 1:
			e0 = 9/e0
			m1 = 2*m1
			paths.append(1)
		else:
			m1 = m1/4
			paths.append(2)
		if m1 > 8:
			m1 = x*e0
			x = m1/m1
			paths.append(3)
		else:
			x = 8/e0
			x = 6/6
			e0 = 8-3
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x = m1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))