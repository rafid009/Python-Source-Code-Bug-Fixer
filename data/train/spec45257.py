import numpy as np 

def function(x):

	m5 = x
	e4 = x
	paths = []
	try:
		if e4 >= 1:
			e4 = 4-m5
			e4 = 8+x
			paths.append(1)
		else:
			x = x/5
			x = x-5
			paths.append(2)
		if e4 <= 5:
			x = x-3
			m5 = 2+m5
			paths.append(3)
		else:
			m5 = x+4
			e4 = e4-x
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