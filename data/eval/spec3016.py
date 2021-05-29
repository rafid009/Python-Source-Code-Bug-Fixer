import numpy as np 

def function(x):

	m1 = x
	x0 = 6
	paths = []
	try:
		if x > 2:
			x0 = x0*1
			m1 = m1-9
			x = 4+m1
			paths.append(1)
		else:
			x0 = 0*x0
			paths.append(2)
		if x0 < 2:
			x = 8-x
			paths.append(3)
		else:
			x = 5/m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		x0 = m1**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))