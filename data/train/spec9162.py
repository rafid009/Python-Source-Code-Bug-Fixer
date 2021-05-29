import numpy as np 

def function(x):

	v4 = 0
	o1 = x
	paths = []
	try:
		if v4 <= 9:
			x = x+1
			x = x-9
			paths.append(1)
		else:
			v4 = 5-7
			o1 = 6*5
			x = 7*x
			paths.append(2)
		if o1 >= 3:
			v4 = v4*x
			x = 4+x
			paths.append(3)
		else:
			v4 = o1-5
			x = o1+8
			v4 = v4+5
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		o1 = v4**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))