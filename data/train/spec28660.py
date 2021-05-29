import numpy as np 

def function(x):

	n1 = 8
	u2 = 3
	x = 1
	paths = []
	try:
		if u2 <= 5:
			u2 = 3-x
			x = 9-x
			u2 = n1-5
			paths.append(1)
		else:
			u2 = u2+x
			paths.append(2)
		if u2 > 3:
			n1 = 7-n1
			paths.append(3)
		else:
			x = x/u2
			u2 = u2-9
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))