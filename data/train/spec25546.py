import numpy as np 

def function(x):

	m7 = x
	e1 = 5
	paths = []
	try:
		if m7 < 2:
			m7 = m7*e1
			e1 = 6+e1
			paths.append(1)
		else:
			m7 = e1+5
			paths.append(2)
		if m7 > 9:
			e1 = 2*e1
			paths.append(3)
		else:
			e1 = x/2
			paths.append(4)
		paths.append(5)
		assert m7 >= 0
		e1 = m7**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))