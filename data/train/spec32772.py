import numpy as np 

def function(x):

	e1 = x
	m6 = x
	paths = []
	try:
		if x > 0:
			e1 = 2/6
			paths.append(1)
		else:
			x = x-7
			m6 = m6-3
			paths.append(2)
		if e1 < 7:
			x = x+2
			e1 = 7*x
			paths.append(3)
		else:
			x = 8+x
			x = 6*x
			x = x+x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		e1 = m6**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))