import numpy as np 

def function(x):

	t3 = 4
	o6 = x
	paths = []
	try:
		if o6 <= 4:
			x = x-1
			x = x/o6
			paths.append(1)
		else:
			x = x+7
			o6 = 1-o6
			t3 = t3*o6
			paths.append(2)
		if x <= 6:
			o6 = o6*6
			t3 = 2*t3
			paths.append(3)
		else:
			o6 = 5/3
			o6 = o6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))