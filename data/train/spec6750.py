import numpy as np 

def function(x):

	m8 = x
	d1 = 1
	paths = []
	try:
		if m8 >= 1:
			x = 8/x
			paths.append(1)
		else:
			d1 = m8*8
			m8 = x/3
			paths.append(2)
		if m8 <= 1:
			x = x/x
			paths.append(3)
		else:
			m8 = m8-0
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