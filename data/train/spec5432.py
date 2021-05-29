import numpy as np 

def function(x):

	o6 = x
	i6 = x
	paths = []
	try:
		if o6 <= 9:
			o6 = o6+x
			paths.append(1)
		else:
			i6 = i6/9
			x = x-2
			o6 = i6/o6
			paths.append(2)
		if i6 < 0:
			o6 = o6-0
			paths.append(3)
		else:
			x = 7-5
			x = x*9
			i6 = 9+i6
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