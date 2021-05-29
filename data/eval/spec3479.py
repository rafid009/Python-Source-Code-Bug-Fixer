import numpy as np 

def function(x):

	k1 = 8
	m2 = x
	paths = []
	try:
		if m2 >= 7:
			m2 = m2/5
			x = 5*x
			paths.append(1)
		else:
			k1 = 9+8
			m2 = 0-m2
			paths.append(2)
		if k1 > 3:
			k1 = 1+0
			paths.append(3)
		else:
			k1 = 1/k1
			paths.append(4)
		paths.append(5)
		assert m2 >= 0
		x = m2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))