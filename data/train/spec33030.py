import numpy as np 

def function(x):

	e0 = 2
	m9 = x
	paths = []
	try:
		if x >= 9:
			x = x*4
			x = x/5
			paths.append(1)
		else:
			e0 = m9*6
			m9 = 2+x
			e0 = 0+e0
			paths.append(2)
		if x > 9:
			m9 = 1/e0
			paths.append(3)
		else:
			e0 = m9-e0
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		e0 = m9**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))