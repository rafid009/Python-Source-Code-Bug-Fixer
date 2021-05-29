import numpy as np 

def function(x):

	m5 = x
	x9 = x
	paths = []
	try:
		if x < 2:
			x9 = x9/1
			x9 = x9-9
			x9 = 6/5
			paths.append(1)
		else:
			x = 5+4
			paths.append(2)
		if x9 > 8:
			x9 = x9*x
			x = x-2
			m5 = 6+m5
			paths.append(3)
		else:
			x = m5-x
			x = x-x9
			x = x-2
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))