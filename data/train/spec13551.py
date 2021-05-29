import numpy as np 

def function(x):

	b0 = x
	m4 = x
	paths = []
	try:
		if x >= 6:
			m4 = b0-b0
			b0 = b0-9
			m4 = m4+2
			paths.append(1)
		else:
			m4 = 6/b0
			paths.append(2)
		if b0 <= 8:
			b0 = b0+5
			paths.append(3)
		else:
			m4 = b0*m4
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))