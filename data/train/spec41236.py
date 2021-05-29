import numpy as np 

def function(x):

	m9 = 0
	e9 = x
	paths = []
	try:
		if e9 > 2:
			e9 = 6*2
			e9 = 5+9
			paths.append(1)
		else:
			m9 = 3+m9
			e9 = e9/8
			x = 4+4
			paths.append(2)
		if x >= 1:
			x = 4+4
			x = x-1
			x = m9-7
			paths.append(3)
		else:
			x = 7-x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))