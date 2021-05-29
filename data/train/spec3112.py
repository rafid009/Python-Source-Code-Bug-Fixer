import numpy as np 

def function(x):

	w6 = 0
	k3 = x
	paths = []
	try:
		if x <= 4:
			w6 = w6-8
			paths.append(1)
		else:
			w6 = x*9
			paths.append(2)
		if x < 3:
			x = x*w6
			w6 = w6+7
			paths.append(3)
		else:
			w6 = k3/w6
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