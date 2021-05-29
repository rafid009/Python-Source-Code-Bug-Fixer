import numpy as np 

def function(x):

	k7 = 6
	o8 = 7
	paths = []
	try:
		if x <= 1:
			x = x+k7
			x = 3*x
			o8 = x/7
			paths.append(1)
		else:
			x = x-k7
			o8 = x+9
			paths.append(2)
		if o8 < 8:
			x = x+o8
			paths.append(3)
		else:
			o8 = o8+1
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		k7 = o8**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))