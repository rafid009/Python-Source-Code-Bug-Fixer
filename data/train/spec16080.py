import numpy as np 

def function(x):

	m3 = x
	q8 = x
	paths = []
	try:
		if x < 7:
			x = 4*x
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if x > 2:
			m3 = x+m3
			paths.append(3)
		else:
			x = x+q8
			m3 = 5+m3
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		x = q8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))