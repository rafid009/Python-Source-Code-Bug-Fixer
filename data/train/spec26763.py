import numpy as np 

def function(x):

	i3 = x
	o6 = x
	paths = []
	try:
		if i3 < 4:
			o6 = 4+o6
			x = x-5
			paths.append(1)
		else:
			o6 = o6*o6
			o6 = x-7
			i3 = i3+o6
			paths.append(2)
		if i3 >= 1:
			o6 = o6*4
			i3 = i3*7
			i3 = o6*o6
			paths.append(3)
		else:
			o6 = o6-6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))