import numpy as np 

def function(x):

	l8 = x
	m9 = x
	paths = []
	try:
		if l8 >= 0:
			l8 = l8*5
			l8 = 5/5
			x = x+6
			paths.append(1)
		else:
			l8 = l8*m9
			x = 9-l8
			paths.append(2)
		if m9 <= 8:
			x = 2*x
			l8 = l8/x
			m9 = 7+0
			paths.append(3)
		else:
			m9 = m9-0
			x = x+8
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		m9 = l8**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))