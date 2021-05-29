import numpy as np 

def function(x):

	k5 = x
	m9 = 5
	paths = []
	try:
		if x < 1:
			x = k5*5
			paths.append(1)
		else:
			k5 = k5/9
			x = x-7
			paths.append(2)
		if x >= 8:
			x = 4/x
			x = x-7
			x = 0-7
			paths.append(3)
		else:
			x = 5+x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		m9 = k5**0.5
		return m9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))