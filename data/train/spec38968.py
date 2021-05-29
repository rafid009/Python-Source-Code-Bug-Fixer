import numpy as np 

def function(x):

	o2 = x
	x9 = 2
	paths = []
	try:
		if o2 <= 5:
			o2 = x9-o2
			paths.append(1)
		else:
			x9 = x9-3
			o2 = o2-7
			x9 = x9/1
			paths.append(2)
		if x < 9:
			x = x+8
			paths.append(3)
		else:
			x9 = x9/o2
			x9 = x9*o2
			x = x9/8
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))