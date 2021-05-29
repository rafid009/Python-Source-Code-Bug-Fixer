import numpy as np 

def function(x):

	k2 = x
	n7 = x
	x = 1
	paths = []
	try:
		if n7 >= 5:
			x = 3+x
			paths.append(1)
		else:
			k2 = k2/1
			x = k2+0
			paths.append(2)
		if x <= 5:
			n7 = n7*5
			x = n7*0
			paths.append(3)
		else:
			x = 3*8
			n7 = 2-n7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		x = n7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))