import numpy as np 

def function(x):

	f9 = 6
	m9 = 5
	paths = []
	try:
		if x >= 4:
			m9 = x+1
			paths.append(1)
		else:
			f9 = m9-f9
			f9 = f9*8
			paths.append(2)
		if x >= 7:
			x = x*5
			f9 = f9-8
			m9 = f9*m9
			paths.append(3)
		else:
			x = 1-x
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