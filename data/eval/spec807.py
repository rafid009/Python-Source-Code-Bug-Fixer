import numpy as np 

def function(x):

	o7 = x
	d5 = 3
	paths = []
	try:
		if x > 3:
			o7 = o7-1
			o7 = o7+0
			paths.append(1)
		else:
			x = x+x
			o7 = o7-2
			x = 8+7
			paths.append(2)
		if o7 > 7:
			o7 = o7*0
			d5 = 1+o7
			paths.append(3)
		else:
			o7 = x/o7
			d5 = d5/d5
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))