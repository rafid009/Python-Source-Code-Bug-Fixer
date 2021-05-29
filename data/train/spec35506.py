import numpy as np 

def function(x):

	h8 = 2
	m4 = 2
	paths = []
	try:
		if m4 > 3:
			m4 = 9*x
			h8 = 5*5
			m4 = m4+2
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if x > 3:
			m4 = m4+m4
			paths.append(3)
		else:
			h8 = x*h8
			m4 = m4/x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))