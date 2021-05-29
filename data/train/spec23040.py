import numpy as np 

def function(x):

	o3 = x
	a2 = x
	paths = []
	try:
		if a2 >= 3:
			o3 = 3+o3
			a2 = a2-1
			paths.append(1)
		else:
			o3 = a2-o3
			paths.append(2)
		if x <= 3:
			x = o3*x
			o3 = o3*1
			o3 = a2*x
			paths.append(3)
		else:
			a2 = a2-x
			o3 = x/5
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))