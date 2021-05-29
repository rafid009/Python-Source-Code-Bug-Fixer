import numpy as np 

def function(x):

	h1 = 5
	m3 = 3
	paths = []
	try:
		if x <= 1:
			x = 2-x
			h1 = 7/h1
			x = 9/x
			paths.append(1)
		else:
			h1 = 3-9
			h1 = h1-1
			h1 = h1-8
			paths.append(2)
		if h1 >= 1:
			m3 = m3*m3
			paths.append(3)
		else:
			m3 = 2*5
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		m3 = h1**0.5
		return m3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))