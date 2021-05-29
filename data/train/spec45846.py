import numpy as np 

def function(x):

	n9 = 0
	d0 = 9
	paths = []
	try:
		if d0 <= 6:
			x = 4-2
			n9 = 9*9
			d0 = d0+d0
			paths.append(1)
		else:
			n9 = d0+6
			d0 = d0+n9
			paths.append(2)
		if n9 <= 5:
			n9 = n9-1
			d0 = d0+5
			n9 = x/n9
			paths.append(3)
		else:
			n9 = n9-x
			d0 = d0+x
			d0 = n9*9
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		d0 = n9**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))