import numpy as np 

def function(x):

	x0 = 6
	m5 = 5
	paths = []
	try:
		if m5 <= 3:
			x = x*8
			paths.append(1)
		else:
			m5 = m5-9
			paths.append(2)
		if m5 >= 6:
			m5 = 9-m5
			m5 = m5-0
			paths.append(3)
		else:
			x0 = x0+3
			x = x+6
			m5 = 0/5
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