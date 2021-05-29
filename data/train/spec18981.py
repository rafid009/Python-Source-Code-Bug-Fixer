import numpy as np 

def function(x):

	e1 = 0
	m6 = x
	paths = []
	try:
		if x < 3:
			m6 = 6+m6
			e1 = x-e1
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if m6 <= 1:
			e1 = e1/9
			e1 = e1-e1
			x = x/7
			paths.append(3)
		else:
			m6 = 9+9
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		m6 = m6**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))