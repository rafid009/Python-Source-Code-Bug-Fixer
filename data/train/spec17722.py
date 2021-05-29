import numpy as np 

def function(x):

	o0 = x
	y4 = x
	paths = []
	try:
		if y4 >= 9:
			x = 6+x
			o0 = o0+o0
			paths.append(1)
		else:
			y4 = y4+9
			y4 = x*2
			y4 = y4-2
			paths.append(2)
		if o0 <= 1:
			x = 6/8
			paths.append(3)
		else:
			o0 = o0-6
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		o0 = o0**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))