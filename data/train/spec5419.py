import numpy as np 

def function(x):

	e1 = x
	m5 = 1
	paths = []
	try:
		if x < 9:
			x = 7/x
			x = x*1
			e1 = 9/e1
			paths.append(1)
		else:
			x = 7/8
			m5 = m5+m5
			paths.append(2)
		if m5 < 5:
			m5 = e1/m5
			m5 = x*m5
			paths.append(3)
		else:
			x = x-x
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