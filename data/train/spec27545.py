import numpy as np 

def function(x):

	m0 = x
	m5 = 8
	paths = []
	try:
		if x > 2:
			x = 6/x
			m5 = 5+2
			m5 = 8-9
			paths.append(1)
		else:
			x = 5*x
			x = x-2
			x = x*6
			paths.append(2)
		if m0 >= 4:
			m5 = m5/m0
			paths.append(3)
		else:
			m0 = 5/m0
			m5 = m5/4
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