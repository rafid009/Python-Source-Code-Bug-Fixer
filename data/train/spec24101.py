import numpy as np 

def function(x):

	m3 = x
	n7 = x
	paths = []
	try:
		if m3 >= 8:
			m3 = 0-4
			x = 5+n7
			paths.append(1)
		else:
			n7 = x/6
			n7 = m3+6
			m3 = 5+m3
			paths.append(2)
		if n7 >= 3:
			m3 = m3*x
			paths.append(3)
		else:
			x = x*7
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