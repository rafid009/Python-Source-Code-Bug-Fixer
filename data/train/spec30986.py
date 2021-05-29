import numpy as np 

def function(x):

	o2 = 1
	n7 = x
	paths = []
	try:
		if o2 < 6:
			o2 = o2/3
			o2 = n7+o2
			paths.append(1)
		else:
			n7 = 7*n7
			paths.append(2)
		if n7 > 8:
			x = x-9
			x = x-3
			x = x*n7
			paths.append(3)
		else:
			o2 = o2-o2
			o2 = n7*2
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		n7 = o2**0.5
		return n7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))