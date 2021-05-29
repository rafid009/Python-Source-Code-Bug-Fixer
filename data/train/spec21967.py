import numpy as np 

def function(x):

	m9 = 3
	j0 = x
	paths = []
	try:
		if j0 <= 2:
			m9 = x/m9
			j0 = j0+7
			paths.append(1)
		else:
			x = j0+x
			paths.append(2)
		if j0 >= 9:
			x = 2-x
			m9 = j0-x
			paths.append(3)
		else:
			x = 7*x
			x = x*8
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))