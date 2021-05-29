import numpy as np 

def function(x):

	t3 = x
	m6 = 8
	paths = []
	try:
		if x <= 3:
			m6 = 3-x
			x = x+t3
			paths.append(1)
		else:
			m6 = m6/m6
			m6 = x-1
			m6 = 1-8
			paths.append(2)
		if t3 > 5:
			m6 = m6+3
			paths.append(3)
		else:
			m6 = t3/m6
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		m6 = t3**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))