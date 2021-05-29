import numpy as np 

def function(x):

	h2 = 5
	m8 = x
	paths = []
	try:
		if h2 <= 6:
			x = 2-x
			x = x+3
			paths.append(1)
		else:
			x = x+x
			x = 6+x
			paths.append(2)
		if h2 >= 0:
			h2 = 0/h2
			x = x*1
			h2 = 3+m8
			paths.append(3)
		else:
			h2 = h2+m8
			m8 = m8/m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))