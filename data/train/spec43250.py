import numpy as np 

def function(x):

	m9 = 7
	l5 = 6
	paths = []
	try:
		if l5 > 0:
			m9 = m9*7
			l5 = l5+l5
			l5 = x+l5
			paths.append(1)
		else:
			x = x-m9
			paths.append(2)
		if x > 9:
			x = x*8
			l5 = l5/l5
			l5 = l5/6
			paths.append(3)
		else:
			m9 = x*m9
			m9 = m9+x
			m9 = 5-x
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