import numpy as np 

def function(x):

	i9 = 8
	m2 = x
	paths = []
	try:
		if i9 >= 0:
			i9 = i9-5
			paths.append(1)
		else:
			i9 = 9+m2
			i9 = 3/i9
			paths.append(2)
		if i9 > 5:
			m2 = m2+x
			i9 = 9/6
			x = 3+x
			paths.append(3)
		else:
			m2 = m2/6
			i9 = i9*6
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))