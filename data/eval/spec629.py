import numpy as np 

def function(x):

	f7 = x
	n5 = 4
	paths = []
	try:
		if f7 < 1:
			n5 = 2+n5
			paths.append(1)
		else:
			n5 = n5/2
			x = 9+1
			paths.append(2)
		if x > 0:
			f7 = f7*6
			paths.append(3)
		else:
			f7 = 2-7
			n5 = n5*x
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))