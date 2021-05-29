import numpy as np 

def function(x):

	b8 = x
	o3 = 2
	paths = []
	try:
		if b8 >= 2:
			o3 = o3*2
			x = 6/3
			x = x*4
			paths.append(1)
		else:
			o3 = 4+6
			x = o3/x
			o3 = 7*9
			paths.append(2)
		if x <= 8:
			o3 = 8*5
			b8 = x+7
			paths.append(3)
		else:
			o3 = 8*x
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))