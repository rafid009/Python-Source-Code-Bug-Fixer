import numpy as np 

def function(x):

	o2 = 3
	i1 = 7
	paths = []
	try:
		if o2 >= 4:
			o2 = 0/o2
			i1 = i1+7
			o2 = 8/1
			paths.append(1)
		else:
			i1 = i1-4
			o2 = o2-9
			paths.append(2)
		if i1 <= 5:
			x = i1/x
			paths.append(3)
		else:
			i1 = 3/4
			o2 = 2/o2
			i1 = i1/2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))