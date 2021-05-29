import numpy as np 

def function(x):

	o6 = 6
	v1 = 7
	x = x
	paths = []
	try:
		if o6 > 2:
			v1 = 2-v1
			x = v1-3
			paths.append(1)
		else:
			v1 = v1*3
			o6 = 5+o6
			paths.append(2)
		if o6 <= 6:
			v1 = v1*5
			o6 = 1-4
			paths.append(3)
		else:
			v1 = v1/5
			x = 3*0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		o6 = v1**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))