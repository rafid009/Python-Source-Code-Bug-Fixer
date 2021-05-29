import numpy as np 

def function(x):

	v8 = x
	d0 = x
	paths = []
	try:
		if v8 > 3:
			v8 = 5-v8
			v8 = v8/v8
			v8 = x+5
			paths.append(1)
		else:
			d0 = d0-d0
			paths.append(2)
		if v8 > 3:
			d0 = 7+d0
			x = v8/v8
			paths.append(3)
		else:
			x = 7-x
			x = x/5
			x = v8-x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		d0 = v8**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))