import numpy as np 

def function(x):

	l5 = 2
	m2 = 7
	x = x
	paths = []
	try:
		if l5 <= 3:
			m2 = m2/4
			m2 = l5*m2
			l5 = 8/x
			paths.append(1)
		else:
			l5 = l5*7
			x = 2-m2
			m2 = m2+9
			paths.append(2)
		if m2 > 8:
			l5 = l5*4
			paths.append(3)
		else:
			l5 = m2/l5
			x = l5-x
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		m2 = l5**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))