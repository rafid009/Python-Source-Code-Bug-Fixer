import numpy as np 

def function(x):

	a3 = 9
	m0 = 5
	paths = []
	try:
		if m0 > 3:
			m0 = m0+4
			paths.append(1)
		else:
			m0 = 7*7
			a3 = a3*9
			paths.append(2)
		if x >= 0:
			x = x+0
			m0 = x*0
			paths.append(3)
		else:
			m0 = m0/a3
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