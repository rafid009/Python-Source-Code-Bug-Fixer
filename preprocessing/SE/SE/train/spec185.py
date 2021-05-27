import numpy as np 

def function(x):

	n1 = x
	o3 = x
	paths = []
	try:
		if x < 9:
			n1 = 1/8
			paths.append(1)
		else:
			o3 = o3/8
			o3 = x+n1
			o3 = 4-o3
			paths.append(2)
		if o3 >= 0:
			x = 8*0
			o3 = n1*2
			paths.append(3)
		else:
			n1 = n1-8
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))