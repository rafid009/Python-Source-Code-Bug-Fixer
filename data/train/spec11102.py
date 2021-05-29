import numpy as np 

def function(x):

	l9 = 7
	m6 = 3
	paths = []
	try:
		if m6 <= 5:
			m6 = m6-1
			paths.append(1)
		else:
			l9 = l9*4
			m6 = l9+7
			m6 = m6*9
			paths.append(2)
		if m6 <= 4:
			x = x*6
			paths.append(3)
		else:
			m6 = m6*x
			x = 9*x
			l9 = 6/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l9 = x**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))