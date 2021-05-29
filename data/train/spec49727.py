import numpy as np 

def function(x):

	o3 = 1
	t4 = x
	paths = []
	try:
		if o3 < 2:
			x = x-8
			o3 = 9/2
			paths.append(1)
		else:
			t4 = o3-x
			o3 = o3-3
			o3 = t4+1
			paths.append(2)
		if o3 >= 5:
			x = 1-x
			t4 = t4-o3
			paths.append(3)
		else:
			x = 0/o3
			o3 = 5-o3
			o3 = 2-o3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		o3 = t4**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))