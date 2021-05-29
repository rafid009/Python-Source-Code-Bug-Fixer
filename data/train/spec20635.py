import numpy as np 

def function(x):

	m9 = x
	a9 = 3
	paths = []
	try:
		if a9 <= 2:
			a9 = x-x
			a9 = m9/1
			a9 = a9-a9
			paths.append(1)
		else:
			x = x+9
			a9 = a9+5
			x = a9+x
			paths.append(2)
		if x <= 0:
			a9 = m9*6
			a9 = 9-4
			paths.append(3)
		else:
			m9 = 5+m9
			m9 = a9*a9
			a9 = a9*4
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