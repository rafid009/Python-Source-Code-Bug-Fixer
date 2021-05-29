import numpy as np 

def function(x):

	m1 = x
	d5 = 6
	paths = []
	try:
		if m1 <= 5:
			d5 = d5+d5
			m1 = m1/5
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if x >= 0:
			m1 = m1-9
			x = x*2
			paths.append(3)
		else:
			d5 = 9-d5
			m1 = 0-m1
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