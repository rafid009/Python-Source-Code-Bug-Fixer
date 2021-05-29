import numpy as np 

def function(x):

	o9 = 1
	n7 = x
	paths = []
	try:
		if o9 <= 1:
			x = 4*2
			paths.append(1)
		else:
			o9 = o9/9
			paths.append(2)
		if n7 >= 5:
			x = n7/o9
			n7 = n7/n7
			o9 = o9+7
			paths.append(3)
		else:
			o9 = 1/6
			o9 = 2/5
			o9 = o9*0
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		o9 = n7**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))