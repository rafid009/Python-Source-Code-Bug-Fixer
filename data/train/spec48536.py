import numpy as np 

def function(x):

	y8 = x
	d1 = 0
	paths = []
	try:
		if d1 < 1:
			y8 = y8+y8
			paths.append(1)
		else:
			d1 = x+d1
			paths.append(2)
		if d1 <= 1:
			y8 = d1/4
			x = 5-x
			y8 = y8-9
			paths.append(3)
		else:
			x = x/d1
			y8 = 8*1
			y8 = y8*0
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		d1 = y8**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))