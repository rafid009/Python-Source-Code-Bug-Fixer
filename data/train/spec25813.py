import numpy as np 

def function(x):

	b1 = x
	m0 = 1
	x = 8
	paths = []
	try:
		if b1 <= 2:
			x = x-3
			b1 = b1/6
			b1 = 1+b1
			paths.append(1)
		else:
			m0 = m0*1
			m0 = m0+5
			m0 = 4+m0
			paths.append(2)
		if b1 >= 6:
			m0 = x-m0
			paths.append(3)
		else:
			b1 = b1*6
			x = 8+6
			x = b1-6
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))