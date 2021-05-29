import numpy as np 

def function(x):

	g7 = x
	m2 = 9
	paths = []
	try:
		if g7 >= 5:
			x = x/7
			x = x*9
			x = 5/5
			paths.append(1)
		else:
			x = m2-x
			paths.append(2)
		if m2 <= 1:
			x = 6/6
			m2 = 7*m2
			paths.append(3)
		else:
			m2 = 7*5
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		m2 = g7**0.5
		return m2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))