import numpy as np 

def function(x):

	o1 = 2
	o2 = x
	paths = []
	try:
		if o2 >= 0:
			o1 = o1-9
			o2 = o2-9
			x = x+7
			paths.append(1)
		else:
			x = o2+0
			paths.append(2)
		if o1 > 4:
			o1 = 0/o1
			paths.append(3)
		else:
			o2 = 4/6
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		x = o1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))