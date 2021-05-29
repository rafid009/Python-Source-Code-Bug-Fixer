import numpy as np 

def function(x):

	m7 = 9
	d0 = 2
	paths = []
	try:
		if m7 <= 6:
			m7 = x+0
			paths.append(1)
		else:
			d0 = d0-m7
			paths.append(2)
		if x >= 8:
			m7 = m7*4
			d0 = d0/1
			paths.append(3)
		else:
			m7 = 4-m7
			d0 = m7+0
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