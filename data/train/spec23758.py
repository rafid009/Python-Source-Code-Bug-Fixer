import numpy as np 

def function(x):

	d7 = x
	n2 = x
	paths = []
	try:
		if x < 5:
			n2 = 4-n2
			x = x+0
			paths.append(1)
		else:
			n2 = n2+d7
			paths.append(2)
		if n2 >= 3:
			n2 = d7*6
			paths.append(3)
		else:
			d7 = d7-0
			x = x*3
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		d7 = n2**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))