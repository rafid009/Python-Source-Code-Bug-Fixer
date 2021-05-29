import numpy as np 

def function(x):

	m5 = x
	e8 = 8
	paths = []
	try:
		if x >= 4:
			x = 4-x
			paths.append(1)
		else:
			x = m5*m5
			m5 = m5+m5
			paths.append(2)
		if x >= 3:
			m5 = 1-m5
			e8 = 2+2
			e8 = 4/6
			paths.append(3)
		else:
			x = 8*x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		e8 = m5**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))