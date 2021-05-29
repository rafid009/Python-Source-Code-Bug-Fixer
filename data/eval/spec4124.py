import numpy as np 

def function(x):

	m6 = x
	u3 = 3
	paths = []
	try:
		if m6 <= 9:
			x = x/7
			x = u3*u3
			m6 = 3*m6
			paths.append(1)
		else:
			x = 3/x
			x = x+9
			m6 = m6*9
			paths.append(2)
		if m6 < 0:
			x = m6/x
			m6 = m6*9
			x = x+6
			paths.append(3)
		else:
			u3 = 8-x
			u3 = m6/u3
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		m6 = u3**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))