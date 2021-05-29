import numpy as np 

def function(x):

	m8 = x
	o8 = x
	paths = []
	try:
		if x >= 3:
			o8 = o8-o8
			x = x*m8
			x = x*5
			paths.append(1)
		else:
			m8 = 1+o8
			paths.append(2)
		if x <= 5:
			m8 = 9/m8
			o8 = o8/m8
			paths.append(3)
		else:
			o8 = 6+o8
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