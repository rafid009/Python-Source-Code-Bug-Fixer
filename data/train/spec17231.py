import numpy as np 

def function(x):

	a9 = 4
	m4 = x
	paths = []
	try:
		if x >= 0:
			m4 = m4*m4
			paths.append(1)
		else:
			m4 = a9+m4
			a9 = x+3
			m4 = m4+a9
			paths.append(2)
		if m4 > 5:
			x = x+7
			a9 = m4/a9
			a9 = 3+a9
			paths.append(3)
		else:
			m4 = m4*7
			x = a9*9
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		a9 = m4**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))