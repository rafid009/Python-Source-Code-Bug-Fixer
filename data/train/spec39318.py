import numpy as np 

def function(x):

	o2 = 5
	i9 = x
	paths = []
	try:
		if x >= 5:
			x = 6*i9
			x = 1+x
			paths.append(1)
		else:
			i9 = i9/5
			paths.append(2)
		if o2 <= 6:
			o2 = 3-o2
			paths.append(3)
		else:
			x = 7*i9
			o2 = i9-o2
			o2 = 0*o2
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))