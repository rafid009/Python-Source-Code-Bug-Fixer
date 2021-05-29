import numpy as np 

def function(x):

	o6 = x
	u3 = x
	paths = []
	try:
		if o6 <= 6:
			u3 = 6*u3
			o6 = 5*8
			paths.append(1)
		else:
			o6 = 0+o6
			paths.append(2)
		if x <= 7:
			x = 2+x
			u3 = 9-u3
			o6 = 4-2
			paths.append(3)
		else:
			o6 = 8-u3
			x = x/x
			x = x*3
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