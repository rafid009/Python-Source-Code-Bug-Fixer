import numpy as np 

def function(x):

	j5 = x
	m6 = x
	paths = []
	try:
		if m6 > 6:
			x = x+m6
			x = x-1
			paths.append(1)
		else:
			x = 6+m6
			paths.append(2)
		if j5 > 7:
			m6 = x-m6
			m6 = 6-m6
			j5 = j5+8
			paths.append(3)
		else:
			x = 8-j5
			m6 = 6+2
			x = j5-2
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