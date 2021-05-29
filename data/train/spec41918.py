import numpy as np 

def function(x):

	n3 = 1
	d1 = 7
	x = x
	paths = []
	try:
		if x >= 6:
			n3 = n3+2
			d1 = d1*2
			x = x*7
			paths.append(1)
		else:
			x = x/1
			x = x/d1
			n3 = 9-n3
			paths.append(2)
		if n3 > 1:
			n3 = n3-x
			paths.append(3)
		else:
			d1 = d1*d1
			d1 = d1*3
			d1 = 2-d1
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))