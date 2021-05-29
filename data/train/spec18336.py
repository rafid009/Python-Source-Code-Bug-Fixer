import numpy as np 

def function(x):

	m2 = 2
	e1 = 6
	paths = []
	try:
		if e1 >= 0:
			m2 = m2-x
			x = 3+x
			x = 4*x
			paths.append(1)
		else:
			e1 = 9/e1
			e1 = 3*e1
			paths.append(2)
		if e1 > 5:
			e1 = 0-e1
			m2 = m2-e1
			m2 = m2+2
			paths.append(3)
		else:
			m2 = 4*0
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		e1 = m2**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))