import numpy as np 

def function(x):

	m2 = 0
	d2 = 3
	paths = []
	try:
		if x <= 4:
			d2 = d2+7
			paths.append(1)
		else:
			d2 = d2+4
			paths.append(2)
		if d2 >= 5:
			d2 = 3-d2
			x = 7-x
			m2 = d2-5
			paths.append(3)
		else:
			m2 = m2+5
			d2 = d2*x
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d2 = d2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))