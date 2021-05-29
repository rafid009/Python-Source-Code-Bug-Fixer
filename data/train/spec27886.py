import numpy as np 

def function(x):

	o1 = 6
	x9 = 6
	paths = []
	try:
		if x >= 5:
			o1 = 5-3
			paths.append(1)
		else:
			x9 = x9*2
			x9 = x9/x
			x9 = x9-x
			paths.append(2)
		if o1 >= 1:
			o1 = x/o1
			o1 = o1/9
			paths.append(3)
		else:
			o1 = 6-x
			o1 = o1*0
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		o1 = x9**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))