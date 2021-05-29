import numpy as np 

def function(x):

	m6 = x
	l6 = x
	paths = []
	try:
		if l6 <= 9:
			m6 = m6+2
			m6 = m6*l6
			l6 = l6/5
			paths.append(1)
		else:
			l6 = 9*l6
			l6 = l6-x
			m6 = 0*m6
			paths.append(2)
		if l6 >= 3:
			x = 2/x
			l6 = l6*5
			paths.append(3)
		else:
			l6 = l6/2
			m6 = x*5
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))