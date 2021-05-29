import numpy as np 

def function(x):

	m2 = 4
	n7 = 2
	x = 0
	paths = []
	try:
		if m2 < 6:
			n7 = 9/n7
			n7 = x*n7
			x = x+5
			paths.append(1)
		else:
			n7 = n7+x
			m2 = n7-9
			m2 = m2+n7
			paths.append(2)
		if x > 0:
			n7 = 2-5
			paths.append(3)
		else:
			n7 = n7+x
			m2 = x*x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		n7 = n7**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))