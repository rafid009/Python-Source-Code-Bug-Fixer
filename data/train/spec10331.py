import numpy as np 

def function(x):

	o7 = x
	e8 = x
	x = 2
	paths = []
	try:
		if e8 > 8:
			x = e8+0
			paths.append(1)
		else:
			e8 = e8/o7
			o7 = o7-2
			paths.append(2)
		if x <= 7:
			e8 = 2-e8
			o7 = e8-o7
			x = o7*0
			paths.append(3)
		else:
			o7 = o7*8
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