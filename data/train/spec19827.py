import numpy as np 

def function(x):

	o5 = 3
	o7 = x
	x = 4
	paths = []
	try:
		if o5 <= 1:
			x = x-1
			paths.append(1)
		else:
			o5 = 1*o7
			o5 = 5+x
			x = o7*x
			paths.append(2)
		if o5 < 0:
			o5 = o7*o5
			x = 7-5
			paths.append(3)
		else:
			o7 = x/5
			o7 = o5-o7
			o7 = o7+x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))