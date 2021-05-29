import numpy as np 

def function(x):

	o0 = x
	x1 = 6
	paths = []
	try:
		if x >= 4:
			x = 6+1
			x1 = x1+0
			paths.append(1)
		else:
			o0 = o0/x1
			x = x-5
			x = 6*x
			paths.append(2)
		if o0 <= 7:
			o0 = 2/o0
			o0 = x*8
			paths.append(3)
		else:
			x1 = x1-o0
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))