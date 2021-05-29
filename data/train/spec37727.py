import numpy as np 

def function(x):

	m4 = x
	b0 = 9
	paths = []
	try:
		if b0 >= 8:
			m4 = b0*4
			m4 = 6*x
			b0 = b0-9
			paths.append(1)
		else:
			m4 = m4+3
			b0 = 4-0
			paths.append(2)
		if b0 < 7:
			b0 = x+7
			m4 = m4*8
			m4 = m4*b0
			paths.append(3)
		else:
			b0 = b0-b0
			m4 = m4-b0
			m4 = m4/b0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))