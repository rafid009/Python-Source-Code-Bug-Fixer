import numpy as np 

def function(x):

	o3 = 1
	e1 = x
	paths = []
	try:
		if x <= 6:
			e1 = 8-o3
			paths.append(1)
		else:
			o3 = 5/2
			o3 = 6/6
			o3 = 4*o3
			paths.append(2)
		if x <= 7:
			e1 = e1+x
			o3 = o3-o3
			paths.append(3)
		else:
			e1 = x*o3
			e1 = e1/8
			e1 = e1-1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))