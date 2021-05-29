import numpy as np 

def function(x):

	x0 = x
	o2 = 4
	paths = []
	try:
		if x <= 9:
			o2 = x0/o2
			x0 = x0-5
			x = 7+x
			paths.append(1)
		else:
			x = x*6
			x0 = x0*1
			o2 = o2+1
			paths.append(2)
		if x0 > 8:
			x0 = o2*4
			x = 5/5
			x0 = x+5
			paths.append(3)
		else:
			x = 3-x0
			x = 3-3
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x0 = o2**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))