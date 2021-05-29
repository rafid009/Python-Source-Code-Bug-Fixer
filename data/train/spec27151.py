import numpy as np 

def function(x):

	m6 = x
	m9 = 2
	x = 1
	paths = []
	try:
		if m6 <= 4:
			m6 = m9+m9
			paths.append(1)
		else:
			m6 = 4-m6
			paths.append(2)
		if x >= 5:
			m9 = 5+7
			x = m6+x
			paths.append(3)
		else:
			m9 = 9-m9
			m6 = m6/7
			m9 = 7/5
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