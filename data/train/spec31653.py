import numpy as np 

def function(x):

	m5 = 6
	h4 = 7
	paths = []
	try:
		if x < 0:
			h4 = x*5
			m5 = m5+h4
			paths.append(1)
		else:
			h4 = h4-h4
			h4 = 9-h4
			m5 = m5/x
			paths.append(2)
		if x >= 4:
			m5 = m5*0
			x = 7-x
			h4 = h4/x
			paths.append(3)
		else:
			x = x-5
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