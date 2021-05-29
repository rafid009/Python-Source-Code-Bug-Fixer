import numpy as np 

def function(x):

	n5 = 2
	m3 = x
	paths = []
	try:
		if m3 <= 1:
			n5 = n5/4
			paths.append(1)
		else:
			m3 = 7+m3
			paths.append(2)
		if x >= 6:
			x = 3*x
			n5 = n5+1
			paths.append(3)
		else:
			n5 = x-n5
			m3 = 5+m3
			x = x*m3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))