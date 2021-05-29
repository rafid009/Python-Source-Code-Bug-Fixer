import numpy as np 

def function(x):

	b8 = 0
	m2 = x
	paths = []
	try:
		if b8 < 2:
			b8 = x*5
			paths.append(1)
		else:
			x = 4/x
			x = 6/x
			m2 = 9/m2
			paths.append(2)
		if x >= 2:
			b8 = 1/b8
			paths.append(3)
		else:
			b8 = b8-m2
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		m2 = b8**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))