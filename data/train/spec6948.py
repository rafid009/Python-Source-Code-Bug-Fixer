import numpy as np 

def function(x):

	a1 = 6
	m3 = x
	paths = []
	try:
		if m3 >= 4:
			a1 = a1*5
			m3 = 4/6
			paths.append(1)
		else:
			m3 = m3+5
			paths.append(2)
		if m3 >= 0:
			x = a1-3
			m3 = 2+5
			a1 = a1*3
			paths.append(3)
		else:
			m3 = 2*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))