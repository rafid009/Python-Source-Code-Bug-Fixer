import numpy as np 

def function(x):

	b3 = 4
	m1 = 0
	paths = []
	try:
		if m1 > 7:
			b3 = b3/m1
			x = 3-x
			paths.append(1)
		else:
			x = b3/x
			b3 = b3*x
			paths.append(2)
		if b3 >= 5:
			x = 7-b3
			b3 = b3+x
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))