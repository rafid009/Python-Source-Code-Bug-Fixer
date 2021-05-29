import numpy as np 

def function(x):

	r5 = x
	o2 = x
	paths = []
	try:
		if x >= 2:
			o2 = 3+o2
			x = 4-x
			r5 = r5/5
			paths.append(1)
		else:
			r5 = 4+1
			x = x+7
			paths.append(2)
		if x > 5:
			o2 = 9/o2
			r5 = 6+6
			o2 = 0/6
			paths.append(3)
		else:
			x = x-3
			r5 = o2+r5
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))