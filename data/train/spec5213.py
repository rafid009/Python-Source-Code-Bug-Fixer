import numpy as np 

def function(x):

	a6 = 3
	m4 = 9
	paths = []
	try:
		if x <= 8:
			a6 = a6*7
			x = x*a6
			x = x+2
			paths.append(1)
		else:
			a6 = x+a6
			x = x+a6
			x = x/5
			paths.append(2)
		if x >= 7:
			m4 = m4/a6
			x = x/x
			paths.append(3)
		else:
			m4 = x+7
			a6 = a6-3
			a6 = a6-m4
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		m4 = m4**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))