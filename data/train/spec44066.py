import numpy as np 

def function(x):

	d7 = x
	m0 = x
	paths = []
	try:
		if x < 0:
			x = 5*6
			paths.append(1)
		else:
			m0 = 9-d7
			d7 = d7+7
			x = x/x
			paths.append(2)
		if m0 <= 6:
			d7 = 5/m0
			d7 = x*d7
			paths.append(3)
		else:
			d7 = d7+1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		d7 = m0**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))