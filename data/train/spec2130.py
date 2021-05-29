import numpy as np 

def function(x):

	o3 = 5
	o0 = 8
	paths = []
	try:
		if o0 < 5:
			o0 = o0-o0
			o3 = o3+2
			paths.append(1)
		else:
			x = x*7
			x = 3*4
			o0 = 9/o0
			paths.append(2)
		if o3 >= 1:
			o3 = 0-o3
			x = 6+x
			o0 = x*1
			paths.append(3)
		else:
			x = 3-x
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o0 = o3**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))