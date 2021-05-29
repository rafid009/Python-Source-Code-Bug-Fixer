import numpy as np 

def function(x):

	d7 = 8
	k1 = x
	paths = []
	try:
		if x > 9:
			x = k1*3
			paths.append(1)
		else:
			x = 1-9
			k1 = k1*d7
			paths.append(2)
		if d7 <= 0:
			d7 = d7+9
			k1 = k1+k1
			paths.append(3)
		else:
			x = 3-9
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