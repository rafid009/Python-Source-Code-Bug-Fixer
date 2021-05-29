import numpy as np 

def function(x):

	x6 = 7
	o0 = 4
	paths = []
	try:
		if x6 >= 4:
			x6 = x6/9
			x6 = x6+9
			paths.append(1)
		else:
			x6 = 5/x6
			paths.append(2)
		if x <= 1:
			x6 = x6*1
			o0 = o0-8
			x6 = o0*7
			paths.append(3)
		else:
			x6 = x6+6
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		o0 = x6**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))