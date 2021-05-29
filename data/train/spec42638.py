import numpy as np 

def function(x):

	o6 = x
	v8 = 4
	paths = []
	try:
		if o6 > 6:
			v8 = o6-v8
			x = x/5
			o6 = o6+1
			paths.append(1)
		else:
			v8 = o6-v8
			x = x-4
			v8 = v8*5
			paths.append(2)
		if o6 >= 2:
			v8 = x/o6
			x = 4/v8
			paths.append(3)
		else:
			v8 = 5-5
			o6 = o6+7
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		o6 = v8**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))