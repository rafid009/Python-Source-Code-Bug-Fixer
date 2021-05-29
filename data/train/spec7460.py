import numpy as np 

def function(x):

	d1 = 8
	v8 = x
	paths = []
	try:
		if x >= 9:
			d1 = d1/9
			paths.append(1)
		else:
			d1 = d1/x
			d1 = d1+v8
			paths.append(2)
		if x >= 2:
			v8 = 4-v8
			d1 = x*x
			v8 = 9*v8
			paths.append(3)
		else:
			v8 = x/v8
			x = 7/8
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))