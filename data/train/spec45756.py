import numpy as np 

def function(x):

	e2 = 8
	m1 = x
	paths = []
	try:
		if e2 <= 5:
			x = 6-x
			e2 = 7/5
			paths.append(1)
		else:
			e2 = e2*2
			paths.append(2)
		if e2 <= 8:
			e2 = e2-m1
			e2 = e2*x
			paths.append(3)
		else:
			m1 = m1/m1
			e2 = 8*x
			e2 = e2+0
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