import numpy as np 

def function(x):

	v7 = 1
	o2 = x
	paths = []
	try:
		if o2 <= 0:
			x = 4-x
			v7 = v7+3
			o2 = v7*o2
			paths.append(1)
		else:
			x = x*8
			v7 = x/v7
			paths.append(2)
		if v7 > 6:
			x = x+2
			o2 = o2*5
			paths.append(3)
		else:
			o2 = o2*2
			o2 = 7+o2
			o2 = o2*9
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