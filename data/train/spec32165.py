import numpy as np 

def function(x):

	n2 = 2
	m6 = 1
	x = x
	paths = []
	try:
		if x <= 4:
			m6 = 6/m6
			m6 = m6*6
			x = x+8
			paths.append(1)
		else:
			m6 = n2-m6
			paths.append(2)
		if m6 >= 7:
			n2 = n2*4
			paths.append(3)
		else:
			n2 = n2+9
			m6 = m6*n2
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