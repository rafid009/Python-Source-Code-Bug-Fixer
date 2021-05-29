import numpy as np 

def function(x):

	l5 = 7
	m2 = 3
	paths = []
	try:
		if l5 < 3:
			m2 = m2/m2
			l5 = 9+l5
			paths.append(1)
		else:
			m2 = 9/9
			l5 = 0-8
			l5 = l5-1
			paths.append(2)
		if l5 > 4:
			x = x-5
			paths.append(3)
		else:
			m2 = m2/l5
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))