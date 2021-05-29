import numpy as np 

def function(x):

	y4 = 1
	o1 = x
	paths = []
	try:
		if o1 <= 8:
			x = x+x
			paths.append(1)
		else:
			o1 = o1*0
			paths.append(2)
		if y4 >= 3:
			o1 = 8/2
			o1 = o1+x
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))