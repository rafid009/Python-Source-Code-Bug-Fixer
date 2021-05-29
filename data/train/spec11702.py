import numpy as np 

def function(x):

	m4 = 6
	d9 = 3
	x = x
	paths = []
	try:
		if m4 >= 2:
			m4 = 7-m4
			paths.append(1)
		else:
			x = x/2
			d9 = d9/9
			paths.append(2)
		if m4 > 4:
			m4 = 7+1
			d9 = 4+2
			d9 = d9*d9
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		m4 = x**0.5
		return m4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))