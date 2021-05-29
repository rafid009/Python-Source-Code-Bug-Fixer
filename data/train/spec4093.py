import numpy as np 

def function(x):

	o9 = 7
	r5 = x
	paths = []
	try:
		if x > 5:
			o9 = o9+2
			x = x+r5
			r5 = r5+3
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if o9 < 5:
			r5 = 3+r5
			paths.append(3)
		else:
			o9 = r5*x
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