import numpy as np 

def function(x):

	r5 = 2
	i6 = x
	paths = []
	try:
		if x <= 9:
			x = x-5
			paths.append(1)
		else:
			r5 = r5-9
			i6 = 5/x
			i6 = i6*1
			paths.append(2)
		if i6 >= 4:
			x = x/r5
			r5 = i6-7
			x = 8/7
			paths.append(3)
		else:
			i6 = 3*i6
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))