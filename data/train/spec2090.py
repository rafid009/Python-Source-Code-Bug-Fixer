import numpy as np 

def function(x):

	o6 = x
	r2 = x
	paths = []
	try:
		if x >= 9:
			r2 = r2/5
			paths.append(1)
		else:
			x = x*r2
			x = 1*r2
			paths.append(2)
		if o6 < 9:
			o6 = o6+9
			o6 = o6-2
			r2 = 5+r2
			paths.append(3)
		else:
			r2 = 8+r2
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))