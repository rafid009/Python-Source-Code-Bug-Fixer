import numpy as np 

def function(x):

	o6 = 9
	b7 = x
	paths = []
	try:
		if b7 < 6:
			o6 = o6*b7
			paths.append(1)
		else:
			o6 = o6*6
			x = x/3
			o6 = o6+3
			paths.append(2)
		if b7 <= 8:
			b7 = 1/b7
			x = o6-2
			paths.append(3)
		else:
			o6 = o6*5
			b7 = 1+1
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