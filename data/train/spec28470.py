import numpy as np 

def function(x):

	n6 = 5
	n7 = x
	paths = []
	try:
		if n7 > 5:
			x = x*x
			paths.append(1)
		else:
			n6 = 9+n6
			n7 = 0/1
			paths.append(2)
		if x > 0:
			x = n7*8
			n6 = 9+n7
			x = x*0
			paths.append(3)
		else:
			n7 = n7*n7
			n6 = x*n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n7 = n6**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))