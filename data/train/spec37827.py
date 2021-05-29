import numpy as np 

def function(x):

	m5 = 6
	b7 = x
	paths = []
	try:
		if x < 1:
			m5 = m5*7
			paths.append(1)
		else:
			b7 = x+b7
			paths.append(2)
		if m5 < 3:
			b7 = 6+b7
			x = 9/x
			m5 = m5*m5
			paths.append(3)
		else:
			x = x+b7
			x = 9*x
			m5 = m5-x
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