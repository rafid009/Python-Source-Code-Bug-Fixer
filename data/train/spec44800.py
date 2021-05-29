import numpy as np 

def function(x):

	o4 = x
	t2 = 8
	paths = []
	try:
		if o4 > 5:
			x = 7+x
			paths.append(1)
		else:
			o4 = o4*5
			x = t2*2
			o4 = x*o4
			paths.append(2)
		if x >= 3:
			x = x+5
			t2 = x/t2
			x = 8-x
			paths.append(3)
		else:
			x = x+2
			o4 = 1/o4
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))