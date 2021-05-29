import numpy as np 

def function(x):

	m6 = x
	j4 = x
	paths = []
	try:
		if m6 <= 0:
			j4 = 6*j4
			j4 = j4*1
			j4 = 7*m6
			paths.append(1)
		else:
			m6 = x+5
			x = 0-x
			paths.append(2)
		if m6 <= 6:
			x = 2-x
			x = j4*8
			j4 = j4+9
			paths.append(3)
		else:
			m6 = x+m6
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