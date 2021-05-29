import numpy as np 

def function(x):

	a5 = x
	m3 = x
	paths = []
	try:
		if a5 > 4:
			a5 = 8+m3
			paths.append(1)
		else:
			x = x*7
			m3 = 2/7
			paths.append(2)
		if m3 < 4:
			a5 = a5/4
			a5 = x/2
			paths.append(3)
		else:
			x = x-0
			m3 = 0-8
			a5 = a5+4
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