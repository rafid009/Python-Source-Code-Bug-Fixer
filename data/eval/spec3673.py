import numpy as np 

def function(x):

	o6 = 6
	f0 = x
	paths = []
	try:
		if f0 <= 5:
			o6 = o6*9
			paths.append(1)
		else:
			o6 = f0-x
			paths.append(2)
		if o6 >= 6:
			o6 = 7-o6
			o6 = x+8
			x = 8/6
			paths.append(3)
		else:
			o6 = x/5
			o6 = o6+x
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		o6 = f0**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))