import numpy as np 

def function(x):

	o6 = x
	x9 = x
	paths = []
	try:
		if x > 1:
			o6 = o6-o6
			x = 0/x9
			paths.append(1)
		else:
			o6 = o6*o6
			paths.append(2)
		if o6 <= 3:
			x9 = 7+x9
			x = o6+9
			x = 8-x
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))