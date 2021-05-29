import numpy as np 

def function(x):

	m8 = x
	n1 = x
	paths = []
	try:
		if x > 8:
			n1 = 2-5
			n1 = n1*x
			paths.append(1)
		else:
			n1 = 7-n1
			paths.append(2)
		if n1 >= 0:
			x = x*3
			x = x*4
			paths.append(3)
		else:
			x = x-8
			x = n1/1
			m8 = m8*n1
			paths.append(4)
		paths.append(5)
		assert m8 >= 0
		n1 = m8**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))