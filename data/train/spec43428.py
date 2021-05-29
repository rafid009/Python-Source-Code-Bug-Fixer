import numpy as np 

def function(x):

	o6 = x
	v1 = 5
	paths = []
	try:
		if x <= 2:
			o6 = v1-v1
			paths.append(1)
		else:
			x = 4+o6
			v1 = 1*v1
			o6 = 6+o6
			paths.append(2)
		if o6 <= 0:
			x = x*x
			x = x*0
			paths.append(3)
		else:
			v1 = 8-v1
			o6 = 0-v1
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		v1 = o6**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))