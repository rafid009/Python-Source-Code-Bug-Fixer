import numpy as np 

def function(x):

	l8 = 8
	m9 = x
	paths = []
	try:
		if x <= 4:
			l8 = m9+4
			x = x+l8
			l8 = m9+m9
			paths.append(1)
		else:
			l8 = l8/l8
			l8 = l8-x
			paths.append(2)
		if x <= 5:
			l8 = x*l8
			m9 = 9*1
			l8 = l8-6
			paths.append(3)
		else:
			m9 = m9-m9
			x = x*1
			x = x+1
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