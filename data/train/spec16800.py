import numpy as np 

def function(x):

	a6 = 8
	m3 = 9
	x = x
	paths = []
	try:
		if x >= 0:
			x = x/x
			m3 = m3+0
			paths.append(1)
		else:
			x = x+7
			a6 = a6+a6
			paths.append(2)
		if x >= 3:
			a6 = 8*m3
			a6 = 3/m3
			paths.append(3)
		else:
			m3 = m3+m3
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