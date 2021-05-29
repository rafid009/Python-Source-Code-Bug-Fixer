import numpy as np 

def function(x):

	n7 = 4
	m7 = x
	paths = []
	try:
		if x < 2:
			n7 = 5*n7
			x = 2-8
			paths.append(1)
		else:
			x = 9/x
			m7 = m7-5
			x = 7+x
			paths.append(2)
		if n7 >= 2:
			n7 = 0-n7
			m7 = m7-1
			paths.append(3)
		else:
			n7 = n7/5
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