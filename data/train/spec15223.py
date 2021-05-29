import numpy as np 

def function(x):

	o7 = x
	r7 = x
	x = 4
	paths = []
	try:
		if x >= 5:
			o7 = o7*0
			x = 6+r7
			o7 = r7*x
			paths.append(1)
		else:
			o7 = o7-2
			paths.append(2)
		if o7 < 1:
			r7 = r7-5
			paths.append(3)
		else:
			r7 = r7+3
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		o7 = o7**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))