import numpy as np 

def function(x):

	i1 = 3
	m1 = 7
	paths = []
	try:
		if x >= 6:
			x = x/8
			m1 = x*7
			i1 = 8/x
			paths.append(1)
		else:
			i1 = 5-i1
			x = x-x
			m1 = 1-0
			paths.append(2)
		if i1 < 6:
			m1 = i1-m1
			paths.append(3)
		else:
			m1 = 3-m1
			paths.append(4)
		paths.append(5)
		assert m1 >= 0
		m1 = m1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))