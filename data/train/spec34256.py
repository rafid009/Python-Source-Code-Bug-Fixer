import numpy as np 

def function(x):

	o6 = 2
	d2 = 2
	paths = []
	try:
		if x > 4:
			o6 = o6+9
			d2 = d2*0
			x = 6*d2
			paths.append(1)
		else:
			o6 = 6*5
			d2 = 6-6
			x = 3-x
			paths.append(2)
		if o6 <= 7:
			d2 = x*o6
			paths.append(3)
		else:
			d2 = 8+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))