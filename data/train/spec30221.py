import numpy as np 

def function(x):

	o6 = x
	x8 = 9
	x = 4
	paths = []
	try:
		if o6 <= 8:
			x8 = x8+o6
			o6 = 4-o6
			paths.append(1)
		else:
			x8 = x8*0
			o6 = 2+o6
			x = x+x
			paths.append(2)
		if x <= 2:
			x = x*8
			paths.append(3)
		else:
			x = 9+x8
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))