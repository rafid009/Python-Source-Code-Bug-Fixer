import numpy as np 

def function(x):

	m2 = x
	v9 = x
	paths = []
	try:
		if x <= 8:
			x = x/3
			x = x-3
			m2 = x-5
			paths.append(1)
		else:
			v9 = v9/7
			m2 = m2/m2
			paths.append(2)
		if m2 >= 9:
			m2 = 4-9
			paths.append(3)
		else:
			v9 = 8+0
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