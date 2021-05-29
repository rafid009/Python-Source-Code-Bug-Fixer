import numpy as np 

def function(x):

	a6 = 7
	m6 = x
	paths = []
	try:
		if x <= 8:
			a6 = 2+a6
			paths.append(1)
		else:
			x = x-m6
			a6 = a6*8
			m6 = a6*m6
			paths.append(2)
		if a6 >= 4:
			x = 7+x
			x = m6/x
			x = m6+x
			paths.append(3)
		else:
			x = 8-x
			x = x-4
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		a6 = m6**0.5
		return a6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))