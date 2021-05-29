import numpy as np 

def function(x):

	u2 = x
	m4 = x
	paths = []
	try:
		if x < 9:
			u2 = u2+5
			paths.append(1)
		else:
			m4 = 1+m4
			m4 = x*u2
			u2 = 0+m4
			paths.append(2)
		if m4 >= 3:
			m4 = m4-u2
			m4 = m4-9
			paths.append(3)
		else:
			u2 = 2+u2
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