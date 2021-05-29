import numpy as np 

def function(x):

	j3 = 7
	m6 = 0
	paths = []
	try:
		if x <= 7:
			m6 = 9+1
			paths.append(1)
		else:
			x = j3+9
			paths.append(2)
		if m6 <= 4:
			m6 = x-5
			paths.append(3)
		else:
			m6 = j3-1
			m6 = m6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m6 = x**0.5
		return m6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))