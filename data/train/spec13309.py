import numpy as np 

def function(x):

	m2 = x
	e8 = 8
	paths = []
	try:
		if x <= 0:
			m2 = e8*7
			paths.append(1)
		else:
			x = 8*9
			e8 = 5+8
			e8 = 6*e8
			paths.append(2)
		if m2 > 5:
			m2 = 6-6
			x = x+2
			paths.append(3)
		else:
			e8 = e8/3
			x = 8+1
			x = m2+m2
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