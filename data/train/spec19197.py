import numpy as np 

def function(x):

	m5 = x
	a5 = 6
	paths = []
	try:
		if m5 < 6:
			m5 = 8+5
			m5 = m5-0
			x = x+4
			paths.append(1)
		else:
			m5 = m5-6
			a5 = a5/x
			paths.append(2)
		if m5 > 5:
			x = x/6
			paths.append(3)
		else:
			x = 4/x
			x = x+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))