import numpy as np 

def function(x):

	m9 = x
	d3 = 1
	paths = []
	try:
		if x < 9:
			x = x-1
			paths.append(1)
		else:
			x = 3/x
			m9 = 3+d3
			x = d3+9
			paths.append(2)
		if x < 6:
			x = 3+m9
			x = x*7
			paths.append(3)
		else:
			m9 = m9-8
			x = x-0
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