import numpy as np 

def function(x):

	o5 = 8
	f2 = x
	paths = []
	try:
		if f2 < 3:
			x = o5+x
			o5 = 2*o5
			f2 = 9/1
			paths.append(1)
		else:
			o5 = 7-0
			paths.append(2)
		if o5 > 0:
			f2 = 4-f2
			x = x/7
			paths.append(3)
		else:
			o5 = o5*x
			x = f2/x
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		x = f2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))