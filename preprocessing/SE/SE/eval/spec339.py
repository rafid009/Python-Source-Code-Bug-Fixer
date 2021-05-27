import numpy as np 

def function(x):

	n8 = x
	k1 = x
	paths = []
	try:
		if x > 7:
			n8 = 8-n8
			x = x+k1
			paths.append(1)
		else:
			n8 = n8/9
			n8 = 0*n8
			paths.append(2)
		if k1 <= 5:
			x = 3/x
			n8 = k1*1
			k1 = 8+n8
			paths.append(3)
		else:
			n8 = n8-x
			n8 = 2/3
			n8 = x*3
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		k1 = n8**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))