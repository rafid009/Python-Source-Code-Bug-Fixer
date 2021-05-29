import numpy as np 

def function(x):

	m1 = x
	e7 = 5
	paths = []
	try:
		if m1 >= 8:
			x = m1*m1
			e7 = 9-9
			m1 = 2/8
			paths.append(1)
		else:
			e7 = e7-8
			paths.append(2)
		if e7 > 7:
			m1 = 3/m1
			e7 = 6-e7
			paths.append(3)
		else:
			e7 = 2*e7
			e7 = e7-3
			e7 = x*e7
			paths.append(4)
		paths.append(5)
		assert e7 >= 0
		x = e7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))