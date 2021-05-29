import numpy as np 

def function(x):

	o1 = x
	v9 = x
	paths = []
	try:
		if v9 <= 4:
			x = x-7
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if o1 > 6:
			v9 = v9*7
			paths.append(3)
		else:
			o1 = 6/7
			o1 = x-o1
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		o1 = v9**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))