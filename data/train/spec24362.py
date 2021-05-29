import numpy as np 

def function(x):

	m2 = x
	l5 = 6
	paths = []
	try:
		if m2 <= 0:
			m2 = m2-9
			l5 = l5-5
			paths.append(1)
		else:
			m2 = m2+5
			l5 = 3-5
			paths.append(2)
		if x >= 0:
			m2 = m2*9
			x = 0*l5
			paths.append(3)
		else:
			m2 = 4*m2
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