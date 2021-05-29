import numpy as np 

def function(x):

	b5 = 6
	o6 = 4
	paths = []
	try:
		if b5 >= 5:
			o6 = x/1
			b5 = o6-1
			o6 = o6/o6
			paths.append(1)
		else:
			b5 = 1-b5
			o6 = 1/o6
			paths.append(2)
		if b5 < 4:
			o6 = b5*3
			x = x/4
			x = x*4
			paths.append(3)
		else:
			x = 4-2
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))