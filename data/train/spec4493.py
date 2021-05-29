import numpy as np 

def function(x):

	v9 = x
	o8 = 5
	paths = []
	try:
		if o8 <= 3:
			o8 = 0/1
			x = x+2
			o8 = o8+9
			paths.append(1)
		else:
			v9 = 3/v9
			x = o8/x
			paths.append(2)
		if x > 5:
			o8 = 6/o8
			v9 = v9*8
			v9 = x/v9
			paths.append(3)
		else:
			v9 = 0*o8
			v9 = 2-v9
			o8 = 2+o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))