import numpy as np 

def function(x):

	u0 = 4
	i6 = x
	paths = []
	try:
		if x <= 5:
			x = i6+u0
			u0 = 9-2
			u0 = i6+u0
			paths.append(1)
		else:
			u0 = u0+4
			u0 = u0+i6
			i6 = x+1
			paths.append(2)
		if u0 >= 8:
			u0 = i6-8
			paths.append(3)
		else:
			x = x-8
			x = 0*2
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		u0 = i6**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))