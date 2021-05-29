import numpy as np 

def function(x):

	m4 = x
	k1 = x
	x = 4
	paths = []
	try:
		if k1 < 9:
			k1 = m4+1
			x = x*m4
			paths.append(1)
		else:
			k1 = 8*k1
			k1 = k1/m4
			k1 = 1*0
			paths.append(2)
		if x <= 9:
			k1 = k1-k1
			m4 = 2/x
			paths.append(3)
		else:
			x = x*6
			k1 = 8/k1
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))