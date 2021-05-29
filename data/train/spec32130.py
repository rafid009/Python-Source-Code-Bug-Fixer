import numpy as np 

def function(x):

	m5 = 4
	e1 = x
	x = 5
	paths = []
	try:
		if x < 7:
			e1 = 0/7
			paths.append(1)
		else:
			e1 = e1*x
			paths.append(2)
		if e1 <= 9:
			x = x/7
			x = x-8
			m5 = 2-9
			paths.append(3)
		else:
			m5 = m5-m5
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))