import numpy as np 

def function(x):

	o3 = 5
	l3 = 4
	paths = []
	try:
		if l3 >= 7:
			o3 = l3-1
			x = x+0
			paths.append(1)
		else:
			o3 = x+o3
			x = 7-x
			paths.append(2)
		if l3 <= 0:
			l3 = l3+o3
			paths.append(3)
		else:
			x = x*9
			o3 = 4-3
			l3 = 4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))