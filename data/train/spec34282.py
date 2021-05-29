import numpy as np 

def function(x):

	m1 = x
	l4 = x
	paths = []
	try:
		if m1 > 9:
			x = 8-x
			m1 = m1/5
			paths.append(1)
		else:
			x = 8/l4
			l4 = 0+l4
			x = l4/3
			paths.append(2)
		if l4 >= 5:
			m1 = m1*3
			paths.append(3)
		else:
			m1 = m1/9
			m1 = m1*x
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