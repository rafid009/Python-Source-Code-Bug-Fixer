import numpy as np 

def function(x):

	m8 = 2
	b2 = 7
	paths = []
	try:
		if b2 > 4:
			x = x-7
			x = 5+6
			paths.append(1)
		else:
			m8 = m8+7
			b2 = m8*m8
			paths.append(2)
		if b2 >= 1:
			x = 2-1
			x = x+2
			b2 = m8-b2
			paths.append(3)
		else:
			m8 = m8*x
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))