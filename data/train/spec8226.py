import numpy as np 

def function(x):

	a9 = 1
	o9 = x
	paths = []
	try:
		if x <= 5:
			a9 = a9/7
			a9 = 2/a9
			paths.append(1)
		else:
			x = x*a9
			o9 = 7/o9
			paths.append(2)
		if o9 > 7:
			x = o9+2
			x = x/1
			o9 = o9/3
			paths.append(3)
		else:
			x = x*a9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		o9 = o9**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))