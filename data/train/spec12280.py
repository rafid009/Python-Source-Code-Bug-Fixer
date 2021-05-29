import numpy as np 

def function(x):

	m7 = x
	b8 = x
	x = 6
	paths = []
	try:
		if x > 0:
			x = 3*b8
			paths.append(1)
		else:
			m7 = x/9
			m7 = 2/9
			x = 6-x
			paths.append(2)
		if m7 > 3:
			m7 = b8+b8
			b8 = 4*b8
			paths.append(3)
		else:
			x = b8+8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))