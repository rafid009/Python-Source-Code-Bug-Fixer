import numpy as np 

def function(x):

	n9 = 2
	d7 = 2
	paths = []
	try:
		if d7 < 4:
			x = 2*x
			d7 = 7+n9
			n9 = n9+4
			paths.append(1)
		else:
			x = x*5
			n9 = n9-n9
			n9 = n9+x
			paths.append(2)
		if x > 6:
			d7 = d7*2
			d7 = d7+d7
			n9 = x/5
			paths.append(3)
		else:
			n9 = 4-5
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		d7 = n9**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))