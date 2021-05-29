import numpy as np 

def function(x):

	e4 = 8
	m2 = 2
	paths = []
	try:
		if e4 >= 7:
			e4 = 3+x
			m2 = 7*m2
			paths.append(1)
		else:
			x = e4-x
			paths.append(2)
		if m2 <= 6:
			x = x+x
			paths.append(3)
		else:
			e4 = m2+e4
			m2 = m2/x
			x = x-7
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		e4 = m2**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))