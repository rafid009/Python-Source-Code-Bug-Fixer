import numpy as np 

def function(x):

	o2 = x
	r8 = 6
	x = 6
	paths = []
	try:
		if x <= 5:
			o2 = o2*o2
			x = x-9
			x = 8-x
			paths.append(1)
		else:
			r8 = r8*5
			o2 = o2/4
			paths.append(2)
		if x <= 4:
			x = x*3
			paths.append(3)
		else:
			o2 = x*o2
			x = x-r8
			o2 = o2+0
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