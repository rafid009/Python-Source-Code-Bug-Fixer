import numpy as np 

def function(x):

	o8 = x
	v2 = 2
	x = x
	paths = []
	try:
		if v2 <= 7:
			x = x+o8
			x = 5+x
			paths.append(1)
		else:
			o8 = o8+0
			x = x*2
			paths.append(2)
		if o8 <= 7:
			o8 = 6/o8
			v2 = v2-0
			paths.append(3)
		else:
			x = 1-x
			x = x-x
			v2 = x+4
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		v2 = o8**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))