import numpy as np 

def function(x):

	m4 = x
	a8 = 4
	paths = []
	try:
		if a8 >= 5:
			a8 = a8/x
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if m4 > 9:
			x = 3+x
			paths.append(3)
		else:
			m4 = m4/2
			a8 = a8-8
			m4 = m4/9
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		a8 = m4**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))