import numpy as np 

def function(x):

	r7 = x
	o5 = 9
	paths = []
	try:
		if r7 > 1:
			r7 = r7-o5
			paths.append(1)
		else:
			o5 = 4/r7
			r7 = r7+6
			paths.append(2)
		if x < 8:
			x = 1-4
			o5 = x*o5
			paths.append(3)
		else:
			x = 6/4
			r7 = r7+2
			o5 = o5*5
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