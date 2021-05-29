import numpy as np 

def function(x):

	n9 = x
	d4 = x
	paths = []
	try:
		if x > 8:
			n9 = n9*7
			x = d4-x
			x = d4/2
			paths.append(1)
		else:
			d4 = d4*1
			paths.append(2)
		if d4 > 5:
			x = 7*3
			n9 = n9*n9
			n9 = 3+2
			paths.append(3)
		else:
			x = x/8
			n9 = n9+7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		d4 = n9**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))