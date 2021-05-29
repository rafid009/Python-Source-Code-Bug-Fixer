import numpy as np 

def function(x):

	m4 = x
	f7 = x
	paths = []
	try:
		if x < 5:
			f7 = f7-3
			paths.append(1)
		else:
			m4 = m4+3
			m4 = m4-1
			paths.append(2)
		if x < 4:
			x = 5/x
			paths.append(3)
		else:
			f7 = 0/3
			f7 = x-6
			x = x/x
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