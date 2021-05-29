import numpy as np 

def function(x):

	n2 = 6
	m0 = 7
	paths = []
	try:
		if x > 1:
			x = 3/8
			paths.append(1)
		else:
			n2 = 1-n2
			m0 = x*6
			m0 = 1+x
			paths.append(2)
		if m0 <= 3:
			x = x*9
			paths.append(3)
		else:
			n2 = 6/n2
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		m0 = n2**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))