import numpy as np 

def function(x):

	m7 = 7
	x3 = 4
	paths = []
	try:
		if m7 >= 5:
			m7 = 6-x
			x3 = x3+6
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if m7 > 8:
			m7 = m7+x
			x = x*x3
			x = 2/x
			paths.append(3)
		else:
			x3 = 1*9
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		m7 = m7**0.5
		return m7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))