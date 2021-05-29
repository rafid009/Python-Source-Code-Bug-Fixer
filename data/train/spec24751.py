import numpy as np 

def function(x):

	v5 = x
	o7 = x
	x = x
	paths = []
	try:
		if o7 > 5:
			o7 = o7+6
			x = x*v5
			paths.append(1)
		else:
			x = x-3
			v5 = v5+7
			o7 = 1+v5
			paths.append(2)
		if v5 <= 0:
			x = o7-2
			o7 = v5-o7
			o7 = o7*1
			paths.append(3)
		else:
			x = x*4
			v5 = v5/8
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))