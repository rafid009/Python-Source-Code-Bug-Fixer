import numpy as np 

def function(x):

	m6 = x
	x4 = 9
	paths = []
	try:
		if x <= 9:
			m6 = m6+7
			paths.append(1)
		else:
			x4 = 6+x4
			x4 = 4+x
			paths.append(2)
		if x < 2:
			x = 4+3
			m6 = m6-8
			paths.append(3)
		else:
			x = 1+4
			x4 = x4+2
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))