import numpy as np 

def function(x):

	v9 = x
	m3 = x
	paths = []
	try:
		if m3 > 6:
			x = x/4
			v9 = v9-9
			m3 = m3+5
			paths.append(1)
		else:
			x = x/9
			x = 8*8
			paths.append(2)
		if x > 0:
			v9 = v9-1
			x = x-8
			paths.append(3)
		else:
			x = 8-9
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