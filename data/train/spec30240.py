import numpy as np 

def function(x):

	m0 = 4
	k1 = 5
	paths = []
	try:
		if m0 < 4:
			k1 = 7-0
			x = 1-x
			m0 = m0-9
			paths.append(1)
		else:
			k1 = x/x
			paths.append(2)
		if x < 6:
			k1 = 2-5
			m0 = m0+7
			k1 = 1-m0
			paths.append(3)
		else:
			k1 = k1-1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))