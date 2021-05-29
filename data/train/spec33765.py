import numpy as np 

def function(x):

	h6 = x
	m5 = x
	paths = []
	try:
		if m5 >= 9:
			m5 = 0-m5
			x = x+7
			h6 = h6+1
			paths.append(1)
		else:
			x = x-8
			paths.append(2)
		if h6 < 4:
			x = x+0
			x = 0*h6
			paths.append(3)
		else:
			x = x/x
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