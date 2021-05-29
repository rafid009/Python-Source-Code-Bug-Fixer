import numpy as np 

def function(x):

	n7 = 0
	m4 = 8
	paths = []
	try:
		if x > 2:
			m4 = 5-1
			n7 = 5+7
			paths.append(1)
		else:
			n7 = n7+n7
			x = x*8
			paths.append(2)
		if m4 > 2:
			m4 = m4*n7
			m4 = m4*2
			m4 = 7+7
			paths.append(3)
		else:
			m4 = m4-m4
			n7 = n7-n7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n7 = x**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))