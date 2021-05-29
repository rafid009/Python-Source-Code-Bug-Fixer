import numpy as np 

def function(x):

	m6 = x
	j1 = x
	paths = []
	try:
		if m6 <= 4:
			m6 = m6-x
			x = x-5
			paths.append(1)
		else:
			m6 = m6-m6
			paths.append(2)
		if m6 <= 7:
			m6 = x/7
			paths.append(3)
		else:
			j1 = 0/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))