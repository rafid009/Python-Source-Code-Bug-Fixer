import numpy as np 

def function(x):

	v5 = x
	o1 = 5
	paths = []
	try:
		if v5 >= 1:
			o1 = o1+o1
			x = x+v5
			x = x-o1
			paths.append(1)
		else:
			o1 = 2-1
			paths.append(2)
		if v5 <= 2:
			o1 = v5+8
			paths.append(3)
		else:
			o1 = 4*o1
			v5 = o1+7
			v5 = v5/4
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		o1 = v5**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))