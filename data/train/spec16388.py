import numpy as np 

def function(x):

	n1 = 6
	m5 = x
	paths = []
	try:
		if n1 > 8:
			x = x-3
			n1 = 4*2
			n1 = 4-n1
			paths.append(1)
		else:
			x = x+0
			paths.append(2)
		if m5 <= 2:
			m5 = m5*6
			n1 = 9*n1
			paths.append(3)
		else:
			x = 9/x
			n1 = 9-4
			m5 = m5*m5
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		n1 = m5**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))