import numpy as np 

def function(x):

	x1 = x
	m9 = 5
	paths = []
	try:
		if x >= 4:
			x = x1*x1
			m9 = m9*6
			paths.append(1)
		else:
			x = m9-x
			x = x-5
			x = m9/2
			paths.append(2)
		if x <= 3:
			m9 = 3*2
			paths.append(3)
		else:
			m9 = m9*m9
			x1 = x1/x1
			x = 1*m9
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		m9 = x1**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))