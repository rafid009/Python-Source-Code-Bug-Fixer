import numpy as np 

def function(x):

	n1 = x
	m4 = 5
	paths = []
	try:
		if n1 >= 1:
			m4 = m4*2
			n1 = 6*n1
			m4 = m4+5
			paths.append(1)
		else:
			m4 = m4/m4
			n1 = n1/1
			paths.append(2)
		if n1 > 1:
			n1 = n1/3
			x = x/n1
			paths.append(3)
		else:
			m4 = x/4
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))