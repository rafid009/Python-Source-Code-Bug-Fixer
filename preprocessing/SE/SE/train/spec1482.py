import numpy as np 

def function(x):

	m4 = x
	b1 = x
	paths = []
	try:
		if b1 < 6:
			x = 2*x
			x = 6*x
			x = 3+2
			paths.append(1)
		else:
			b1 = 1+m4
			m4 = m4*m4
			paths.append(2)
		if b1 < 4:
			m4 = 7/m4
			x = 9-4
			b1 = 5/b1
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		x = m4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))