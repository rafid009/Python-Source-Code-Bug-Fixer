import numpy as np 

def function(x):

	m5 = 4
	e5 = 9
	paths = []
	try:
		if x >= 1:
			e5 = 6-e5
			paths.append(1)
		else:
			e5 = e5*6
			e5 = 5-e5
			x = x-m5
			paths.append(2)
		if e5 >= 2:
			x = x*9
			e5 = e5+0
			paths.append(3)
		else:
			e5 = e5/1
			m5 = 1-9
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		x = e5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))