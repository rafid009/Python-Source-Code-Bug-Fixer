import numpy as np 

def function(x):

	h4 = x
	m1 = 8
	x = x
	paths = []
	try:
		if h4 > 5:
			m1 = 1+m1
			h4 = h4-1
			paths.append(1)
		else:
			x = x/5
			m1 = m1/h4
			paths.append(2)
		if h4 > 1:
			x = 0/x
			h4 = 4*2
			paths.append(3)
		else:
			h4 = 6-h4
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		h4 = m1**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))