import numpy as np 

def function(x):

	o6 = 8
	u7 = x
	paths = []
	try:
		if o6 <= 6:
			u7 = u7/1
			paths.append(1)
		else:
			u7 = 9+x
			u7 = 2-u7
			u7 = u7-5
			paths.append(2)
		if u7 > 1:
			u7 = 0/o6
			o6 = o6/7
			paths.append(3)
		else:
			o6 = x/o6
			o6 = 8*o6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))