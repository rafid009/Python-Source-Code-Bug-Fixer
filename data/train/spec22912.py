import numpy as np 

def function(x):

	o2 = x
	o5 = x
	paths = []
	try:
		if o2 > 4:
			x = 9*x
			o5 = x*o5
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if o2 < 6:
			o2 = 0*6
			o5 = o5/1
			o2 = o5/o5
			paths.append(3)
		else:
			o2 = x*0
			x = o2*1
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))