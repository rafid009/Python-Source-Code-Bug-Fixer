import numpy as np 

def function(x):

	m8 = x
	d4 = x
	paths = []
	try:
		if x > 7:
			x = x*d4
			d4 = m8-d4
			m8 = m8+9
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if x < 7:
			x = 3+x
			paths.append(3)
		else:
			m8 = 0-m8
			x = 5+5
			d4 = d4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))