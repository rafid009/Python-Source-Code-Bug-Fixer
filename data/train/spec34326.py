import numpy as np 

def function(x):

	o6 = x
	r2 = 8
	paths = []
	try:
		if o6 <= 4:
			r2 = x*r2
			paths.append(1)
		else:
			o6 = 4/o6
			paths.append(2)
		if r2 > 8:
			x = 0*x
			o6 = o6-8
			r2 = r2*7
			paths.append(3)
		else:
			r2 = 6*r2
			o6 = 6/1
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