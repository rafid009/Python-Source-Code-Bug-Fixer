import numpy as np 

def function(x):

	m6 = 0
	d4 = x
	paths = []
	try:
		if x < 4:
			x = x-m6
			m6 = 6/x
			paths.append(1)
		else:
			d4 = d4-8
			paths.append(2)
		if d4 <= 6:
			d4 = 9-d4
			paths.append(3)
		else:
			d4 = d4+0
			paths.append(4)
		paths.append(5)
		assert m6 >= 0
		d4 = m6**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))