import numpy as np 

def function(x):

	q3 = x
	o2 = x
	paths = []
	try:
		if o2 > 4:
			o2 = o2/3
			o2 = o2*x
			paths.append(1)
		else:
			q3 = 6/q3
			x = o2-q3
			paths.append(2)
		if o2 >= 8:
			o2 = 6-o2
			q3 = q3/2
			paths.append(3)
		else:
			x = 6/x
			o2 = o2+7
			o2 = q3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))