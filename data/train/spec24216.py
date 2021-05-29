import numpy as np 

def function(x):

	k5 = x
	r4 = 3
	paths = []
	try:
		if x <= 4:
			x = x/k5
			paths.append(1)
		else:
			r4 = 5*r4
			paths.append(2)
		if r4 < 1:
			k5 = 7/k5
			r4 = 9/1
			paths.append(3)
		else:
			r4 = r4+x
			x = x-3
			r4 = k5*r4
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