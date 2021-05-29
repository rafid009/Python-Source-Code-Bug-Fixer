import numpy as np 

def function(x):

	m0 = 2
	j1 = x
	paths = []
	try:
		if j1 >= 0:
			m0 = 7/9
			m0 = m0/8
			m0 = m0*j1
			paths.append(1)
		else:
			j1 = j1+0
			m0 = j1/j1
			x = 3-3
			paths.append(2)
		if j1 <= 5:
			x = 9*x
			m0 = x+2
			paths.append(3)
		else:
			m0 = 0-m0
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		j1 = m0**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))