import numpy as np 

def function(x):

	f9 = x
	o1 = x
	paths = []
	try:
		if x > 1:
			f9 = x/9
			paths.append(1)
		else:
			o1 = o1*x
			paths.append(2)
		if o1 < 0:
			x = 4/9
			paths.append(3)
		else:
			x = x-o1
			x = 1*5
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		o1 = f9**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))