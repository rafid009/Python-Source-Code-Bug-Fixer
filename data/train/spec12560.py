import numpy as np 

def function(x):

	o3 = 1
	a6 = x
	paths = []
	try:
		if o3 >= 0:
			x = x+6
			o3 = 9-4
			a6 = a6/6
			paths.append(1)
		else:
			x = 6-2
			a6 = a6+0
			a6 = a6-7
			paths.append(2)
		if x < 7:
			a6 = a6+a6
			paths.append(3)
		else:
			o3 = o3-5
			a6 = a6*0
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		o3 = a6**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))