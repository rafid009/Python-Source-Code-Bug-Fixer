import numpy as np 

def function(x):

	m6 = 3
	i7 = 4
	paths = []
	try:
		if m6 >= 1:
			i7 = 9/i7
			paths.append(1)
		else:
			i7 = i7*i7
			m6 = i7*m6
			i7 = i7*i7
			paths.append(2)
		if m6 < 2:
			i7 = 2/i7
			x = m6*i7
			m6 = 8+8
			paths.append(3)
		else:
			i7 = 8*i7
			m6 = 2-8
			x = i7/2
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