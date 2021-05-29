import numpy as np 

def function(x):

	m8 = 0
	j1 = 6
	paths = []
	try:
		if m8 >= 5:
			j1 = x*6
			j1 = 3/m8
			paths.append(1)
		else:
			m8 = 9*1
			m8 = 1/4
			paths.append(2)
		if m8 >= 4:
			x = x-m8
			j1 = 8/j1
			x = x-j1
			paths.append(3)
		else:
			x = 3+x
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