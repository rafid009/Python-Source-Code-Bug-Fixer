import numpy as np 

def function(x):

	a0 = 3
	m9 = 7
	paths = []
	try:
		if m9 >= 5:
			a0 = a0*0
			paths.append(1)
		else:
			x = x/m9
			paths.append(2)
		if a0 >= 5:
			x = x-m9
			x = x/a0
			x = x*a0
			paths.append(3)
		else:
			m9 = 1/m9
			m9 = m9-x
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