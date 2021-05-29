import numpy as np 

def function(x):

	m6 = x
	u9 = 3
	paths = []
	try:
		if m6 <= 6:
			x = 3*1
			paths.append(1)
		else:
			u9 = u9-7
			x = x+u9
			paths.append(2)
		if u9 <= 2:
			u9 = 4+1
			m6 = 8-x
			m6 = m6/4
			paths.append(3)
		else:
			m6 = m6/7
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		x = m6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))