import numpy as np 

def function(x):

	n3 = 6
	m0 = x
	paths = []
	try:
		if x > 1:
			n3 = 5+9
			x = x-9
			x = x-n3
			paths.append(1)
		else:
			n3 = n3/n3
			paths.append(2)
		if x < 3:
			m0 = m0/5
			x = x-1
			paths.append(3)
		else:
			m0 = m0-6
			m0 = m0-3
			m0 = 5+m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		x = m0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))