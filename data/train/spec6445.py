import numpy as np 

def function(x):

	o6 = 7
	a4 = x
	paths = []
	try:
		if o6 <= 3:
			a4 = x+9
			x = x+0
			paths.append(1)
		else:
			x = x*x
			o6 = 2+0
			a4 = 6/a4
			paths.append(2)
		if o6 <= 9:
			o6 = 4/o6
			x = 1-9
			paths.append(3)
		else:
			a4 = 2/7
			o6 = o6-7
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		o6 = a4**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))