import numpy as np 

def function(x):

	h2 = x
	m5 = 9
	paths = []
	try:
		if x > 3:
			h2 = h2*x
			m5 = m5*h2
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if h2 < 3:
			x = x*1
			paths.append(3)
		else:
			x = m5/x
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		x = h2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))