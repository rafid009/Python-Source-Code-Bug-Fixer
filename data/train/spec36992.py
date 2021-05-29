import numpy as np 

def function(x):

	o3 = 7
	a5 = 9
	paths = []
	try:
		if x <= 8:
			o3 = o3+3
			a5 = a5/x
			o3 = o3-7
			paths.append(1)
		else:
			x = 5/x
			x = 9*x
			o3 = o3*x
			paths.append(2)
		if a5 <= 1:
			a5 = a5-6
			x = x/x
			o3 = x-8
			paths.append(3)
		else:
			a5 = 1*x
			o3 = x*6
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		o3 = a5**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))