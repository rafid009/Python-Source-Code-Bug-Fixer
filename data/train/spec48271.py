import numpy as np 

def function(x):

	o1 = 7
	n6 = x
	paths = []
	try:
		if o1 < 5:
			n6 = 7+n6
			paths.append(1)
		else:
			o1 = n6/9
			x = x/x
			paths.append(2)
		if n6 > 7:
			n6 = n6+x
			paths.append(3)
		else:
			o1 = o1/5
			o1 = o1-0
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))