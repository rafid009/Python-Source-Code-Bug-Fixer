import numpy as np 

def function(x):

	k1 = x
	n8 = 3
	paths = []
	try:
		if x > 4:
			k1 = n8-k1
			paths.append(1)
		else:
			n8 = 2/9
			n8 = n8*1
			k1 = n8+k1
			paths.append(2)
		if k1 <= 4:
			n8 = 1*3
			paths.append(3)
		else:
			n8 = x+9
			k1 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))