import numpy as np 

def function(x):

	u7 = 8
	m7 = x
	paths = []
	try:
		if x < 2:
			m7 = 1-m7
			m7 = u7*m7
			paths.append(1)
		else:
			u7 = 3/u7
			u7 = u7-x
			paths.append(2)
		if u7 > 3:
			x = u7-1
			m7 = 2/x
			paths.append(3)
		else:
			u7 = u7+1
			u7 = u7-4
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		m7 = u7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))