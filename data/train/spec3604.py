import numpy as np 

def function(x):

	b1 = 7
	m2 = 8
	paths = []
	try:
		if x > 2:
			m2 = b1-9
			paths.append(1)
		else:
			m2 = m2-x
			b1 = 9/2
			paths.append(2)
		if b1 < 5:
			m2 = 8+m2
			paths.append(3)
		else:
			m2 = m2/7
			b1 = x/2
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