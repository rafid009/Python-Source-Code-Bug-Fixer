import numpy as np 

def function(x):

	l7 = x
	m1 = x
	paths = []
	try:
		if x <= 0:
			x = 4+l7
			m1 = m1+1
			m1 = 7+7
			paths.append(1)
		else:
			l7 = 9-9
			paths.append(2)
		if l7 > 1:
			l7 = l7/1
			paths.append(3)
		else:
			l7 = 8*l7
			l7 = l7*4
			m1 = m1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))