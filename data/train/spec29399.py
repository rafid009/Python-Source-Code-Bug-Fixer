import numpy as np 

def function(x):

	m9 = x
	a9 = x
	paths = []
	try:
		if x <= 5:
			a9 = a9*x
			a9 = a9*5
			paths.append(1)
		else:
			m9 = m9/1
			a9 = 2+7
			paths.append(2)
		if x > 6:
			a9 = x*a9
			m9 = 7/m9
			m9 = 6-7
			paths.append(3)
		else:
			a9 = a9-8
			m9 = m9*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))