import numpy as np 

def function(x):

	d9 = 8
	m9 = x
	paths = []
	try:
		if x > 3:
			m9 = 4+8
			paths.append(1)
		else:
			x = x+1
			paths.append(2)
		if x > 6:
			x = d9*m9
			x = 8-4
			x = 5-m9
			paths.append(3)
		else:
			m9 = 6/m9
			x = 1-x
			d9 = d9-x
			paths.append(4)
		paths.append(5)
		assert m9 >= 0
		x = m9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))