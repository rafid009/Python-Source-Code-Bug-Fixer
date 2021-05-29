import numpy as np 

def function(x):

	e6 = 8
	m5 = x
	paths = []
	try:
		if x > 3:
			m5 = 3+2
			m5 = e6-e6
			e6 = 8-e6
			paths.append(1)
		else:
			e6 = e6+e6
			paths.append(2)
		if m5 >= 5:
			m5 = x+6
			m5 = 1*m5
			paths.append(3)
		else:
			x = x-9
			x = 4-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))