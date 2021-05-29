import numpy as np 

def function(x):

	m5 = x
	d0 = 6
	x = 9
	paths = []
	try:
		if x > 8:
			x = x+3
			paths.append(1)
		else:
			m5 = d0+m5
			paths.append(2)
		if x <= 9:
			m5 = m5*3
			paths.append(3)
		else:
			d0 = 0-d0
			d0 = d0-d0
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))