import numpy as np 

def function(x):

	i3 = 3
	o1 = x
	x = 1
	paths = []
	try:
		if i3 >= 9:
			o1 = o1+x
			o1 = o1+0
			paths.append(1)
		else:
			o1 = 5-o1
			o1 = 7+x
			x = x-4
			paths.append(2)
		if i3 < 6:
			o1 = 5-7
			paths.append(3)
		else:
			x = i3/3
			x = x-2
			o1 = o1-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o1 = x**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))