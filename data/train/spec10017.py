import numpy as np 

def function(x):

	m4 = 7
	d5 = 1
	paths = []
	try:
		if d5 > 0:
			m4 = m4/7
			d5 = 5-d5
			m4 = 9-m4
			paths.append(1)
		else:
			d5 = d5/m4
			x = 3-d5
			paths.append(2)
		if x < 7:
			m4 = 9-m4
			x = x-4
			d5 = 5-9
			paths.append(3)
		else:
			m4 = m4+8
			d5 = 2*d5
			d5 = d5*d5
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))