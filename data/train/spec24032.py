import numpy as np 

def function(x):

	v4 = x
	m6 = x
	x = 3
	paths = []
	try:
		if m6 < 0:
			v4 = 8/8
			x = m6-m6
			paths.append(1)
		else:
			x = 2+x
			paths.append(2)
		if m6 >= 8:
			v4 = v4+6
			v4 = m6-v4
			m6 = 7*m6
			paths.append(3)
		else:
			x = x+6
			x = x+5
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