import numpy as np 

def function(x):

	p1 = x
	o3 = x
	paths = []
	try:
		if o3 < 8:
			o3 = o3-5
			p1 = p1+4
			paths.append(1)
		else:
			p1 = o3+p1
			x = 6/x
			x = x+x
			paths.append(2)
		if x < 2:
			x = x*4
			p1 = p1*9
			x = o3+6
			paths.append(3)
		else:
			o3 = 8-o3
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		o3 = p1**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))