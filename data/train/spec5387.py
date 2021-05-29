import numpy as np 

def function(x):

	o3 = x
	p1 = x
	paths = []
	try:
		if x <= 0:
			o3 = 6-o3
			p1 = p1*o3
			x = x+o3
			paths.append(1)
		else:
			o3 = 4-o3
			p1 = p1-2
			p1 = p1+0
			paths.append(2)
		if p1 < 3:
			x = 8/x
			o3 = p1-o3
			p1 = p1-1
			paths.append(3)
		else:
			x = 5-x
			x = x*7
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