import numpy as np 

def function(x):

	o3 = x
	p6 = 1
	paths = []
	try:
		if p6 >= 4:
			p6 = 7+p6
			x = 5*x
			paths.append(1)
		else:
			o3 = 9/o3
			o3 = 5/x
			o3 = 5-o3
			paths.append(2)
		if o3 > 6:
			p6 = 8/7
			p6 = p6-7
			o3 = p6*p6
			paths.append(3)
		else:
			o3 = x-0
			x = x/p6
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		x = p6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))