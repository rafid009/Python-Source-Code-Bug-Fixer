import numpy as np 

def function(x):

	o6 = 2
	i6 = 1
	paths = []
	try:
		if i6 > 4:
			o6 = i6*o6
			o6 = 7+7
			paths.append(1)
		else:
			o6 = 2/o6
			paths.append(2)
		if i6 <= 1:
			o6 = x/o6
			o6 = o6*3
			paths.append(3)
		else:
			o6 = o6*8
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))