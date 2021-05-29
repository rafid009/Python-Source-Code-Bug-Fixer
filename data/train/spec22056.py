import numpy as np 

def function(x):

	r6 = x
	o6 = x
	paths = []
	try:
		if x >= 1:
			o6 = o6*9
			o6 = o6/4
			paths.append(1)
		else:
			x = r6*8
			paths.append(2)
		if r6 <= 4:
			o6 = o6*7
			paths.append(3)
		else:
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))