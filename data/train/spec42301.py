import numpy as np 

def function(x):

	m6 = 3
	b1 = x
	paths = []
	try:
		if x >= 0:
			b1 = 9+x
			m6 = 5/5
			x = 5+x
			paths.append(1)
		else:
			b1 = x-7
			x = x-2
			x = 6/x
			paths.append(2)
		if x <= 5:
			m6 = b1/7
			b1 = 3/4
			b1 = 5-1
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))