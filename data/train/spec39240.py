import numpy as np 

def function(x):

	k6 = 4
	o8 = 1
	paths = []
	try:
		if x >= 9:
			o8 = o8-3
			k6 = 8+x
			x = x/9
			paths.append(1)
		else:
			o8 = x+1
			k6 = 2/o8
			o8 = o8+3
			paths.append(2)
		if x < 0:
			x = 1-k6
			k6 = k6-o8
			paths.append(3)
		else:
			x = x/6
			x = x/k6
			k6 = 2+o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))