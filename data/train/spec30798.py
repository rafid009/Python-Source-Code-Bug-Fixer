import numpy as np 

def function(x):

	d5 = x
	v1 = x
	x = 8
	paths = []
	try:
		if x >= 5:
			v1 = v1/d5
			v1 = 8+d5
			paths.append(1)
		else:
			d5 = v1*5
			d5 = 4/d5
			d5 = 8*d5
			paths.append(2)
		if d5 < 9:
			x = x+x
			paths.append(3)
		else:
			v1 = v1-7
			x = 6-8
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		d5 = v1**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))