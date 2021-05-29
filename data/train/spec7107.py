import numpy as np 

def function(x):

	d6 = 2
	v4 = 9
	paths = []
	try:
		if x <= 3:
			v4 = v4-d6
			v4 = 7/v4
			x = x*v4
			paths.append(1)
		else:
			v4 = d6-3
			d6 = 7*x
			paths.append(2)
		if v4 > 8:
			d6 = d6-v4
			d6 = d6+0
			x = x+8
			paths.append(3)
		else:
			x = 1*4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		d6 = v4**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))