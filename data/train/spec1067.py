import numpy as np 

def function(x):

	m3 = 2
	e0 = 5
	x = 5
	paths = []
	try:
		if x >= 7:
			e0 = 2*x
			m3 = 3/3
			x = x/x
			paths.append(1)
		else:
			x = m3-x
			paths.append(2)
		if m3 >= 9:
			e0 = 2*e0
			x = x+5
			paths.append(3)
		else:
			x = x+1
			e0 = e0-9
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		x = e0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))