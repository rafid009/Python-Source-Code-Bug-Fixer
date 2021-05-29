import numpy as np 

def function(x):

	o2 = x
	e3 = 9
	paths = []
	try:
		if x < 0:
			x = o2/2
			x = x+2
			e3 = 4-e3
			paths.append(1)
		else:
			o2 = 9*2
			o2 = o2*3
			x = x*x
			paths.append(2)
		if e3 < 0:
			x = x*8
			o2 = o2+7
			e3 = 2+8
			paths.append(3)
		else:
			x = e3-x
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