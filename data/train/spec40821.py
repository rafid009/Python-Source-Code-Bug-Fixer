import numpy as np 

def function(x):

	m3 = x
	b7 = x
	paths = []
	try:
		if x > 4:
			b7 = 5+b7
			b7 = 6/b7
			paths.append(1)
		else:
			x = x-x
			x = x/m3
			m3 = 3+x
			paths.append(2)
		if b7 > 0:
			m3 = x*m3
			paths.append(3)
		else:
			x = 0-b7
			x = x-b7
			b7 = m3*b7
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))