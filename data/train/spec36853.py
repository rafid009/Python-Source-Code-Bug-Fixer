import numpy as np 

def function(x):

	k3 = 3
	q8 = 0
	paths = []
	try:
		if k3 >= 1:
			q8 = 9-x
			paths.append(1)
		else:
			x = 3*6
			paths.append(2)
		if q8 > 0:
			k3 = 3+k3
			x = x*1
			x = 5+q8
			paths.append(3)
		else:
			x = x-0
			x = k3*4
			k3 = 4/5
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		k3 = q8**0.5
		return k3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))