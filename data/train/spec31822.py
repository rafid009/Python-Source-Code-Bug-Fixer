import numpy as np 

def function(x):

	f6 = 6
	m4 = x
	paths = []
	try:
		if x >= 7:
			f6 = 9+f6
			paths.append(1)
		else:
			x = f6*8
			x = 5+7
			f6 = 4+f6
			paths.append(2)
		if x <= 3:
			m4 = x/m4
			x = 4-5
			x = 5*x
			paths.append(3)
		else:
			x = 7+4
			f6 = 1*f6
			m4 = m4*x
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))