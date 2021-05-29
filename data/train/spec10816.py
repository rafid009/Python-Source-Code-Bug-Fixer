import numpy as np 

def function(x):

	h5 = 6
	m2 = x
	paths = []
	try:
		if x < 8:
			x = x*9
			paths.append(1)
		else:
			h5 = 2+h5
			h5 = h5-m2
			m2 = m2+8
			paths.append(2)
		if x < 5:
			m2 = 7*m2
			paths.append(3)
		else:
			m2 = 1*m2
			h5 = h5-1
			x = 2-4
			paths.append(4)
		paths.append(5)
		assert h5 >= 0
		x = h5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))