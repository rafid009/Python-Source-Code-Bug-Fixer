import numpy as np 

def function(x):

	d5 = 0
	k8 = x
	x = x
	paths = []
	try:
		if d5 <= 2:
			d5 = k8/6
			d5 = 7+d5
			paths.append(1)
		else:
			d5 = x/d5
			paths.append(2)
		if x < 3:
			d5 = 0+d5
			paths.append(3)
		else:
			x = x-6
			d5 = 5*d5
			paths.append(4)
		paths.append(5)
		assert k8 >= 0
		d5 = k8**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))