import numpy as np 

def function(x):

	o1 = x
	f1 = 4
	x = 2
	paths = []
	try:
		if o1 >= 0:
			o1 = f1+o1
			o1 = o1*7
			f1 = f1+1
			paths.append(1)
		else:
			f1 = f1*f1
			x = 2/9
			paths.append(2)
		if o1 > 8:
			f1 = f1*6
			o1 = o1*3
			x = x*o1
			paths.append(3)
		else:
			o1 = o1/5
			o1 = o1/9
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