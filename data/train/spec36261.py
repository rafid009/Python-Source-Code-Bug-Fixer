import numpy as np 

def function(x):

	n2 = 4
	o3 = x
	paths = []
	try:
		if n2 <= 3:
			x = 2/x
			n2 = 2+5
			n2 = 7*n2
			paths.append(1)
		else:
			x = x-n2
			n2 = 2*n2
			n2 = 8+n2
			paths.append(2)
		if x <= 3:
			x = 8+x
			x = x*x
			paths.append(3)
		else:
			o3 = o3/3
			x = x+8
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))