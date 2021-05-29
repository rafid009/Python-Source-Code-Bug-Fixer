import numpy as np 

def function(x):

	o6 = 4
	n6 = 9
	paths = []
	try:
		if o6 >= 8:
			x = o6-n6
			x = o6*4
			x = n6*x
			paths.append(1)
		else:
			n6 = x/9
			o6 = o6+5
			paths.append(2)
		if x <= 5:
			n6 = x*o6
			x = x/n6
			n6 = x+n6
			paths.append(3)
		else:
			o6 = 0+n6
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		o6 = n6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))