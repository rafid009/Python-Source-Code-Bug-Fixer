import numpy as np 

def function(x):

	m9 = 0
	p3 = x
	paths = []
	try:
		if m9 > 1:
			p3 = p3*5
			m9 = 9/9
			paths.append(1)
		else:
			p3 = p3/p3
			m9 = m9+5
			m9 = p3-x
			paths.append(2)
		if m9 <= 7:
			m9 = m9*x
			paths.append(3)
		else:
			x = 1/x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		m9 = m9**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))