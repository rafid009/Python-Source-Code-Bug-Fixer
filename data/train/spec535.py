import numpy as np 

def function(x):

	m0 = x
	n5 = x
	paths = []
	try:
		if x > 4:
			m0 = 8/m0
			m0 = 3/m0
			m0 = x*3
			paths.append(1)
		else:
			n5 = n5/3
			n5 = n5+4
			paths.append(2)
		if x >= 8:
			x = x*9
			n5 = n5-n5
			paths.append(3)
		else:
			x = 5+x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		m0 = n5**0.5
		return m0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))