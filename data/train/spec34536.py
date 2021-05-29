import numpy as np 

def function(x):

	v4 = x
	d8 = 5
	x = x
	paths = []
	try:
		if d8 > 3:
			d8 = 9/3
			d8 = d8/2
			paths.append(1)
		else:
			d8 = 8/7
			paths.append(2)
		if v4 >= 9:
			v4 = x/v4
			x = v4/d8
			paths.append(3)
		else:
			x = x/6
			x = 2-v4
			x = v4+x
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))