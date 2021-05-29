import numpy as np 

def function(x):

	m4 = x
	b8 = 9
	paths = []
	try:
		if m4 < 9:
			m4 = 4-1
			paths.append(1)
		else:
			b8 = b8-b8
			x = x-8
			x = 0-2
			paths.append(2)
		if x <= 8:
			b8 = m4-b8
			paths.append(3)
		else:
			m4 = 5+7
			x = 6/x
			m4 = 8*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))