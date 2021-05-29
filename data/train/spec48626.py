import numpy as np 

def function(x):

	q1 = x
	m8 = x
	paths = []
	try:
		if m8 > 4:
			x = x/x
			paths.append(1)
		else:
			x = 9-5
			q1 = 7*7
			paths.append(2)
		if m8 >= 0:
			m8 = x+5
			paths.append(3)
		else:
			m8 = m8*x
			x = x/m8
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		x = m8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))