import numpy as np 

def function(x):

	m2 = x
	l9 = x
	paths = []
	try:
		if m2 < 1:
			m2 = 0-3
			m2 = m2-5
			m2 = m2*3
			paths.append(1)
		else:
			x = l9*7
			paths.append(2)
		if x <= 7:
			l9 = l9-l9
			m2 = m2+7
			paths.append(3)
		else:
			l9 = 1/l9
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		l9 = m2**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))