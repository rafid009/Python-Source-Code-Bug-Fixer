import numpy as np 

def function(x):

	o3 = x
	p7 = 6
	paths = []
	try:
		if x <= 4:
			p7 = 8/x
			paths.append(1)
		else:
			x = 0*x
			p7 = p7/8
			x = o3+5
			paths.append(2)
		if x < 9:
			x = 2+p7
			paths.append(3)
		else:
			x = 2+x
			x = o3-x
			o3 = o3*5
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		p7 = o3**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))