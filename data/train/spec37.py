import numpy as np 

def function(x):

	d1 = x
	m4 = x
	x = 1
	paths = []
	try:
		if x >= 6:
			m4 = 9/m4
			paths.append(1)
		else:
			m4 = m4+1
			d1 = d1-d1
			paths.append(2)
		if x < 7:
			d1 = 9+m4
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert m4 >= 0
		d1 = m4**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))