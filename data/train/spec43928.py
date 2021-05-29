import numpy as np 

def function(x):

	m6 = 7
	e5 = x
	x = x
	paths = []
	try:
		if x >= 6:
			x = e5-2
			e5 = e5+3
			paths.append(1)
		else:
			e5 = e5+m6
			m6 = e5*1
			paths.append(2)
		if m6 >= 3:
			m6 = e5-7
			m6 = m6*0
			m6 = m6/3
			paths.append(3)
		else:
			e5 = 7+e5
			e5 = m6-6
			x = 6-e5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))