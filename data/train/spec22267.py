import numpy as np 

def function(x):

	e5 = x
	m9 = 4
	paths = []
	try:
		if x <= 9:
			m9 = x/9
			paths.append(1)
		else:
			e5 = 3*e5
			m9 = m9*e5
			m9 = 2-x
			paths.append(2)
		if e5 >= 4:
			e5 = m9/8
			paths.append(3)
		else:
			e5 = 3*8
			e5 = x*e5
			paths.append(4)
		paths.append(5)
		assert e5 >= 0
		e5 = e5**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))