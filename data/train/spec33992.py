import numpy as np 

def function(x):

	k3 = x
	o8 = 3
	paths = []
	try:
		if k3 < 1:
			o8 = o8/9
			paths.append(1)
		else:
			o8 = o8-3
			o8 = o8/9
			paths.append(2)
		if o8 <= 1:
			x = 7+1
			o8 = k3/x
			x = 8-6
			paths.append(3)
		else:
			k3 = k3*9
			x = x+k3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		o8 = k3**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))