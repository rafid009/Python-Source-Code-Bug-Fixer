import numpy as np 

def function(x):

	v0 = x
	o5 = 9
	paths = []
	try:
		if v0 >= 9:
			o5 = 5*x
			v0 = v0+v0
			o5 = o5/x
			paths.append(1)
		else:
			o5 = 1+o5
			paths.append(2)
		if v0 > 4:
			v0 = v0/5
			v0 = v0*7
			paths.append(3)
		else:
			o5 = o5+2
			x = x-1
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		o5 = v0**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))