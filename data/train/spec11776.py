import numpy as np 

def function(x):

	o1 = x
	n7 = 0
	paths = []
	try:
		if n7 >= 4:
			x = x/6
			n7 = 5*o1
			paths.append(1)
		else:
			o1 = 3*o1
			n7 = 6+n7
			paths.append(2)
		if o1 < 2:
			o1 = o1*o1
			n7 = n7+7
			o1 = o1-7
			paths.append(3)
		else:
			o1 = 9/o1
			o1 = 2*o1
			x = n7*n7
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))