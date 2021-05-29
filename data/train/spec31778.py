import numpy as np 

def function(x):

	o9 = 7
	n5 = 5
	paths = []
	try:
		if x >= 9:
			o9 = o9*0
			o9 = x+9
			paths.append(1)
		else:
			o9 = x-2
			o9 = o9*3
			paths.append(2)
		if n5 >= 6:
			n5 = x+x
			x = x-0
			x = x*x
			paths.append(3)
		else:
			n5 = x-n5
			x = x+o9
			o9 = 2+0
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