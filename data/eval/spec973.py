import numpy as np 

def function(x):

	m0 = 0
	u0 = x
	x = x
	paths = []
	try:
		if x <= 1:
			m0 = 1-7
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if u0 > 8:
			x = x-m0
			paths.append(3)
		else:
			u0 = u0/2
			x = x-x
			u0 = 9/u0
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		m0 = u0**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))