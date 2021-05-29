import numpy as np 

def function(x):

	l9 = 2
	m0 = x
	paths = []
	try:
		if l9 <= 2:
			x = x+l9
			l9 = l9-0
			paths.append(1)
		else:
			m0 = x+m0
			x = m0-3
			m0 = 9-m0
			paths.append(2)
		if x < 3:
			l9 = l9-l9
			l9 = l9+9
			m0 = 3/m0
			paths.append(3)
		else:
			l9 = l9-7
			x = 8-2
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