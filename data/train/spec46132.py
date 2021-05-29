import numpy as np 

def function(x):

	e1 = x
	m9 = 0
	paths = []
	try:
		if m9 >= 6:
			m9 = m9-0
			e1 = e1*e1
			paths.append(1)
		else:
			x = 2*m9
			paths.append(2)
		if m9 < 9:
			m9 = x*e1
			paths.append(3)
		else:
			e1 = 9+3
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))