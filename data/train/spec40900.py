import numpy as np 

def function(x):

	n5 = 6
	n8 = 6
	paths = []
	try:
		if n5 <= 3:
			x = 8/x
			n5 = n5-n5
			x = x*2
			paths.append(1)
		else:
			n5 = n5-2
			n5 = n5-7
			n5 = 1+n5
			paths.append(2)
		if x > 8:
			x = 1*x
			n8 = n8*1
			paths.append(3)
		else:
			x = 7/x
			n8 = x/4
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