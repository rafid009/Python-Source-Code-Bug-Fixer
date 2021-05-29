import numpy as np 

def function(x):

	g1 = x
	o2 = 9
	paths = []
	try:
		if x >= 5:
			o2 = 1/x
			o2 = o2-g1
			g1 = g1*2
			paths.append(1)
		else:
			x = g1-7
			o2 = 9*2
			g1 = 6/o2
			paths.append(2)
		if o2 > 0:
			o2 = o2*x
			g1 = g1*8
			paths.append(3)
		else:
			x = 7+x
			o2 = 0+1
			o2 = 2*1
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		o2 = o2**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))