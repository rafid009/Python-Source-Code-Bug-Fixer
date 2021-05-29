import numpy as np 

def function(x):

	m1 = x
	h2 = x
	paths = []
	try:
		if m1 >= 4:
			m1 = 0-m1
			h2 = 2-x
			paths.append(1)
		else:
			h2 = h2+2
			paths.append(2)
		if x > 6:
			x = x+6
			m1 = m1+h2
			m1 = m1/h2
			paths.append(3)
		else:
			x = x-0
			m1 = 4/6
			h2 = h2+h2
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