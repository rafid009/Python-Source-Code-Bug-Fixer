import numpy as np 

def function(x):

	o5 = x
	v1 = x
	paths = []
	try:
		if o5 < 1:
			v1 = o5*v1
			paths.append(1)
		else:
			x = 1*x
			x = v1/8
			o5 = 7*o5
			paths.append(2)
		if v1 < 3:
			x = x+v1
			v1 = 4/1
			paths.append(3)
		else:
			v1 = v1/5
			v1 = v1+o5
			v1 = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))