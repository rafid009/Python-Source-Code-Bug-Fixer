import numpy as np 

def function(x):

	m4 = 6
	d7 = x
	paths = []
	try:
		if m4 >= 9:
			d7 = 9/d7
			d7 = d7-0
			d7 = 3+m4
			paths.append(1)
		else:
			d7 = 7/x
			paths.append(2)
		if d7 <= 5:
			x = 7*7
			m4 = 8*m4
			d7 = 9*d7
			paths.append(3)
		else:
			m4 = m4*3
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))