import numpy as np 

def function(x):

	j9 = 6
	m1 = x
	paths = []
	try:
		if x >= 9:
			m1 = m1-9
			paths.append(1)
		else:
			j9 = x-5
			x = j9*5
			paths.append(2)
		if j9 <= 3:
			j9 = j9+1
			j9 = 3-m1
			j9 = j9*4
			paths.append(3)
		else:
			j9 = j9+j9
			j9 = j9*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m1 = x**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))