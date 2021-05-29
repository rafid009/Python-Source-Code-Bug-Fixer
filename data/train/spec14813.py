import numpy as np 

def function(x):

	j1 = 9
	m4 = x
	paths = []
	try:
		if x >= 6:
			j1 = j1*9
			paths.append(1)
		else:
			j1 = 3/j1
			m4 = x-6
			paths.append(2)
		if m4 >= 0:
			j1 = j1/j1
			x = 6+4
			paths.append(3)
		else:
			j1 = j1-1
			m4 = 1/m4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		m4 = j1**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))