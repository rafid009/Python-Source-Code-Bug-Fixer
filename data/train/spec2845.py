import numpy as np 

def function(x):

	k1 = 7
	m8 = 0
	paths = []
	try:
		if x <= 2:
			m8 = m8+4
			k1 = 4+9
			paths.append(1)
		else:
			m8 = m8+x
			paths.append(2)
		if x >= 3:
			x = 5/7
			paths.append(3)
		else:
			x = 0+x
			m8 = m8/x
			m8 = 3+m8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))