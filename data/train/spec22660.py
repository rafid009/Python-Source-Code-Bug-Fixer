import numpy as np 

def function(x):

	a7 = 8
	m8 = 0
	paths = []
	try:
		if x < 0:
			m8 = m8*m8
			x = x/3
			paths.append(1)
		else:
			x = x*3
			a7 = a7/5
			paths.append(2)
		if a7 < 2:
			m8 = m8/6
			paths.append(3)
		else:
			x = 7-a7
			a7 = a7*1
			a7 = 6/a7
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