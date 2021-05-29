import numpy as np 

def function(x):

	m9 = 6
	j0 = 2
	paths = []
	try:
		if x >= 5:
			m9 = 3-5
			m9 = m9-x
			paths.append(1)
		else:
			m9 = m9*m9
			x = 1*0
			j0 = 6*8
			paths.append(2)
		if j0 > 9:
			m9 = m9-4
			x = x-1
			paths.append(3)
		else:
			j0 = j0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))