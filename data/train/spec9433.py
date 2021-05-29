import numpy as np 

def function(x):

	h2 = x
	m1 = x
	paths = []
	try:
		if m1 > 6:
			h2 = h2*3
			h2 = h2*1
			paths.append(1)
		else:
			m1 = m1-h2
			x = x-m1
			h2 = 7/3
			paths.append(2)
		if h2 > 5:
			m1 = 7+7
			x = x/7
			paths.append(3)
		else:
			h2 = h2*4
			h2 = h2/4
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