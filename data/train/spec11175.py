import numpy as np 

def function(x):

	o2 = x
	l2 = 6
	paths = []
	try:
		if o2 >= 5:
			l2 = l2*7
			x = 2-x
			paths.append(1)
		else:
			o2 = o2-0
			paths.append(2)
		if x < 7:
			x = 0+x
			paths.append(3)
		else:
			x = x/o2
			o2 = o2/l2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))