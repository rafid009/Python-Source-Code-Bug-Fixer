import numpy as np 

def function(x):

	o2 = 9
	a4 = x
	paths = []
	try:
		if a4 >= 3:
			x = x/6
			paths.append(1)
		else:
			x = x-o2
			paths.append(2)
		if o2 < 4:
			x = x-0
			o2 = 7-o2
			a4 = a4-5
			paths.append(3)
		else:
			o2 = o2*o2
			x = 4+x
			o2 = 4-6
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		a4 = o2**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))