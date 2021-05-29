import numpy as np 

def function(x):

	m9 = 4
	u2 = 0
	paths = []
	try:
		if x <= 9:
			m9 = m9-x
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if m9 <= 1:
			x = 3+8
			x = 7*1
			paths.append(3)
		else:
			u2 = u2/x
			x = 4+u2
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