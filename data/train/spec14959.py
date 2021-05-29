import numpy as np 

def function(x):

	m5 = x
	e4 = x
	paths = []
	try:
		if x >= 7:
			x = x-1
			m5 = 6+0
			x = x/3
			paths.append(1)
		else:
			e4 = e4/7
			paths.append(2)
		if x >= 7:
			m5 = 5-2
			e4 = e4*5
			paths.append(3)
		else:
			m5 = m5+0
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))