import numpy as np 

def function(x):

	k1 = x
	m0 = x
	x = 3
	paths = []
	try:
		if x <= 7:
			m0 = m0*7
			paths.append(1)
		else:
			k1 = k1+1
			x = 7+x
			k1 = k1+m0
			paths.append(2)
		if k1 < 1:
			x = x-2
			paths.append(3)
		else:
			m0 = 9*1
			paths.append(4)
		paths.append(5)
		assert m0 >= 0
		k1 = m0**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))