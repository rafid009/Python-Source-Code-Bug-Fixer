import numpy as np 

def function(x):

	k1 = 2
	n9 = x
	paths = []
	try:
		if k1 >= 3:
			k1 = k1/2
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if x < 4:
			n9 = x*5
			x = x*1
			paths.append(3)
		else:
			k1 = x/x
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		n9 = n9**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))