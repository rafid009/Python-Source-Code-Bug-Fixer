import numpy as np 

def function(x):

	k5 = 6
	m2 = x
	paths = []
	try:
		if k5 > 6:
			m2 = m2*m2
			k5 = 3/k5
			m2 = m2+x
			paths.append(1)
		else:
			x = x-5
			m2 = 1/6
			paths.append(2)
		if x >= 3:
			k5 = x/k5
			k5 = 2/k5
			paths.append(3)
		else:
			k5 = k5-0
			k5 = k5*3
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))