import numpy as np 

def function(x):

	m1 = x
	k1 = x
	paths = []
	try:
		if m1 <= 4:
			m1 = m1+3
			m1 = 1-m1
			paths.append(1)
		else:
			k1 = m1+2
			paths.append(2)
		if k1 >= 5:
			m1 = m1*6
			paths.append(3)
		else:
			m1 = x/7
			k1 = k1+k1
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