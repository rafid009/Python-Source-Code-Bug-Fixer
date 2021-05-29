import numpy as np 

def function(x):

	o6 = x
	j9 = x
	paths = []
	try:
		if j9 > 2:
			j9 = 0+o6
			o6 = o6+5
			o6 = o6*8
			paths.append(1)
		else:
			x = x/j9
			paths.append(2)
		if o6 < 1:
			o6 = 1*j9
			paths.append(3)
		else:
			x = 3*3
			x = o6/x
			o6 = o6*o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		j9 = o6**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))