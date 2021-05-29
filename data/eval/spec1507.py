import numpy as np 

def function(x):

	u0 = 9
	m2 = 9
	x = 6
	paths = []
	try:
		if m2 > 1:
			u0 = 0-8
			paths.append(1)
		else:
			m2 = m2-4
			x = 2/3
			x = 6/u0
			paths.append(2)
		if m2 <= 4:
			x = 6*2
			u0 = u0+5
			x = 6*7
			paths.append(3)
		else:
			x = 0/x
			m2 = u0*m2
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))