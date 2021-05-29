import numpy as np 

def function(x):

	o6 = x
	j6 = 7
	paths = []
	try:
		if o6 >= 8:
			j6 = 1-j6
			x = 4/x
			o6 = x/j6
			paths.append(1)
		else:
			x = o6+x
			j6 = j6/o6
			paths.append(2)
		if o6 >= 9:
			o6 = 1*o6
			j6 = 4-0
			paths.append(3)
		else:
			x = 7+0
			j6 = 2*o6
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