import numpy as np 

def function(x):

	f8 = 7
	m6 = x
	paths = []
	try:
		if x > 3:
			f8 = m6*m6
			f8 = f8+2
			paths.append(1)
		else:
			f8 = 7-0
			paths.append(2)
		if f8 < 1:
			x = x*f8
			f8 = 9-f8
			m6 = 8/m6
			paths.append(3)
		else:
			f8 = m6+5
			m6 = 6/f8
			x = m6-x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))