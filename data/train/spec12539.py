import numpy as np 

def function(x):

	n9 = x
	m6 = 4
	paths = []
	try:
		if m6 < 1:
			m6 = m6*5
			paths.append(1)
		else:
			m6 = m6/2
			n9 = 8*n9
			paths.append(2)
		if x < 6:
			x = 8*x
			n9 = n9*4
			x = x+n9
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))