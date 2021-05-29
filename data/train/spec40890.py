import numpy as np 

def function(x):

	o6 = 1
	i6 = x
	paths = []
	try:
		if o6 >= 7:
			i6 = o6/9
			paths.append(1)
		else:
			o6 = o6+8
			o6 = 3+o6
			x = o6-8
			paths.append(2)
		if o6 <= 7:
			o6 = 5+o6
			i6 = 3+i6
			x = x*i6
			paths.append(3)
		else:
			o6 = 1/o6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		x = i6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))