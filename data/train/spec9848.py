import numpy as np 

def function(x):

	r2 = x
	o1 = 2
	paths = []
	try:
		if x >= 7:
			o1 = o1*o1
			x = x-9
			paths.append(1)
		else:
			x = x/o1
			o1 = o1-5
			r2 = r2/6
			paths.append(2)
		if o1 > 6:
			x = x+2
			x = x+8
			x = 2+x
			paths.append(3)
		else:
			x = r2+x
			o1 = r2/1
			x = o1*o1
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