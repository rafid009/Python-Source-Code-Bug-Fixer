import numpy as np 

def function(x):

	u2 = x
	m8 = x
	paths = []
	try:
		if x < 7:
			u2 = 9-m8
			m8 = 0-6
			x = 6*8
			paths.append(1)
		else:
			x = x/8
			x = x-3
			x = 4*8
			paths.append(2)
		if u2 > 0:
			x = m8/7
			paths.append(3)
		else:
			m8 = 5*u2
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))