import numpy as np 

def function(x):

	n0 = 7
	m6 = 4
	paths = []
	try:
		if x < 1:
			n0 = n0/2
			n0 = n0+2
			m6 = m6-7
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x > 9:
			x = 4+m6
			paths.append(3)
		else:
			n0 = 1-n0
			m6 = m6*4
			x = x*2
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))