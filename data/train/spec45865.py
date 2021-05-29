import numpy as np 

def function(x):

	m2 = 8
	l8 = x
	paths = []
	try:
		if l8 < 7:
			m2 = m2+9
			x = 2/x
			l8 = x+x
			paths.append(1)
		else:
			l8 = l8+4
			l8 = l8-3
			paths.append(2)
		if x <= 7:
			l8 = l8-6
			paths.append(3)
		else:
			m2 = 5/5
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))