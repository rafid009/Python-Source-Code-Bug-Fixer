import numpy as np 

def function(x):

	m6 = x
	b7 = 2
	x = x
	paths = []
	try:
		if x <= 1:
			x = 5+x
			paths.append(1)
		else:
			m6 = 0*2
			b7 = b7-2
			x = x-1
			paths.append(2)
		if x >= 9:
			b7 = 0+9
			m6 = x/x
			paths.append(3)
		else:
			b7 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))