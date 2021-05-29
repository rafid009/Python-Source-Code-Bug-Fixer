import numpy as np 

def function(x):

	m3 = 3
	a7 = x
	paths = []
	try:
		if m3 >= 7:
			m3 = 8*m3
			m3 = 3*4
			x = x/x
			paths.append(1)
		else:
			m3 = m3+2
			a7 = 0*m3
			a7 = 9-9
			paths.append(2)
		if a7 > 8:
			m3 = a7+2
			x = 1-m3
			x = 1/x
			paths.append(3)
		else:
			a7 = 6/3
			x = x*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))