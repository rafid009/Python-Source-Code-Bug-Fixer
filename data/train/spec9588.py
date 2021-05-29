import numpy as np 

def function(x):

	a7 = 8
	o5 = 4
	paths = []
	try:
		if a7 < 5:
			x = 3+x
			o5 = 6/o5
			o5 = o5+6
			paths.append(1)
		else:
			x = a7/9
			paths.append(2)
		if o5 <= 7:
			o5 = 5-8
			x = x*x
			paths.append(3)
		else:
			a7 = a7-6
			o5 = o5+2
			o5 = 3/2
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))