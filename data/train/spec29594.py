import numpy as np 

def function(x):

	d3 = 1
	u8 = x
	paths = []
	try:
		if u8 >= 4:
			u8 = u8-2
			paths.append(1)
		else:
			d3 = d3-d3
			paths.append(2)
		if u8 >= 3:
			u8 = x*3
			paths.append(3)
		else:
			d3 = d3+1
			x = 2+x
			d3 = 7/4
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))