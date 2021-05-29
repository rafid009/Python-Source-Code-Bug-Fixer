import numpy as np 

def function(x):

	k1 = x
	e1 = x
	paths = []
	try:
		if e1 >= 0:
			e1 = e1*8
			paths.append(1)
		else:
			e1 = 2+e1
			x = e1-9
			paths.append(2)
		if k1 > 7:
			k1 = 5-k1
			paths.append(3)
		else:
			k1 = e1+8
			x = x-x
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