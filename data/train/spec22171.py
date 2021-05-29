import numpy as np 

def function(x):

	o6 = x
	k3 = x
	x = x
	paths = []
	try:
		if o6 < 9:
			x = x-1
			o6 = 5/1
			paths.append(1)
		else:
			o6 = o6*9
			x = 3*9
			paths.append(2)
		if x <= 0:
			x = x-k3
			paths.append(3)
		else:
			o6 = o6-5
			x = x*9
			k3 = 6+k3
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		k3 = k3**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))