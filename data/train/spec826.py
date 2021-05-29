import numpy as np 

def function(x):

	f3 = x
	o5 = x
	x = 2
	paths = []
	try:
		if x <= 1:
			o5 = f3/9
			x = x-6
			paths.append(1)
		else:
			o5 = o5/o5
			paths.append(2)
		if x >= 8:
			o5 = o5-8
			o5 = 2/o5
			o5 = f3+o5
			paths.append(3)
		else:
			o5 = o5*1
			o5 = 0+f3
			x = x+7
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))