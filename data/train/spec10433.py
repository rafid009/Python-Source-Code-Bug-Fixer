import numpy as np 

def function(x):

	r6 = x
	k5 = 0
	paths = []
	try:
		if k5 >= 4:
			x = x-x
			r6 = r6/2
			k5 = 5/k5
			paths.append(1)
		else:
			x = x-7
			r6 = r6-r6
			paths.append(2)
		if k5 <= 8:
			k5 = x/4
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))