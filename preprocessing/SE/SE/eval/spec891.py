import numpy as np 

def function(x):

	r8 = x
	o6 = 7
	x = x
	paths = []
	try:
		if o6 <= 8:
			o6 = o6/o6
			o6 = 7+r8
			o6 = r8-1
			paths.append(1)
		else:
			o6 = o6-4
			paths.append(2)
		if x > 9:
			r8 = 1+4
			r8 = x-r8
			r8 = r8+6
			paths.append(3)
		else:
			o6 = r8/x
			o6 = r8+o6
			x = 1*4
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))