import numpy as np 

def function(x):

	m0 = 8
	k5 = x
	paths = []
	try:
		if x <= 8:
			m0 = 1+8
			paths.append(1)
		else:
			k5 = k5/k5
			paths.append(2)
		if m0 >= 7:
			x = 8/5
			x = x/6
			x = 0-8
			paths.append(3)
		else:
			k5 = m0+1
			k5 = 6+k5
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))