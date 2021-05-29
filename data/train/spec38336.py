import numpy as np 

def function(x):

	z6 = 6
	m8 = 8
	x = x
	paths = []
	try:
		if z6 > 9:
			x = x/7
			paths.append(1)
		else:
			x = x/2
			m8 = m8*m8
			m8 = m8*8
			paths.append(2)
		if m8 > 1:
			m8 = 3/x
			x = x/z6
			m8 = 1+m8
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		z6 = m8**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))