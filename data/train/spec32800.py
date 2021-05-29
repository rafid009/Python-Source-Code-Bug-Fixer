import numpy as np 

def function(x):

	h2 = 1
	m2 = 1
	paths = []
	try:
		if x > 1:
			h2 = 7*2
			paths.append(1)
		else:
			m2 = m2*0
			paths.append(2)
		if h2 < 0:
			h2 = h2-5
			paths.append(3)
		else:
			m2 = m2/6
			h2 = 1*h2
			h2 = x+7
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