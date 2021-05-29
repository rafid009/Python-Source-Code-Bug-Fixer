import numpy as np 

def function(x):

	h1 = 1
	m1 = x
	paths = []
	try:
		if m1 > 0:
			m1 = 1*7
			x = x/7
			h1 = x/2
			paths.append(1)
		else:
			h1 = h1-0
			h1 = 2+h1
			paths.append(2)
		if m1 >= 3:
			m1 = m1-m1
			m1 = m1*5
			paths.append(3)
		else:
			x = 6+x
			h1 = h1/7
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