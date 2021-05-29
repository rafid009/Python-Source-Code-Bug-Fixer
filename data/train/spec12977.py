import numpy as np 

def function(x):

	n2 = 8
	r5 = 6
	paths = []
	try:
		if r5 <= 8:
			n2 = r5-n2
			x = x+7
			r5 = r5-0
			paths.append(1)
		else:
			x = 3-x
			paths.append(2)
		if n2 > 6:
			r5 = r5/x
			paths.append(3)
		else:
			x = x*5
			x = 5/7
			x = x+7
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))