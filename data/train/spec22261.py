import numpy as np 

def function(x):

	o0 = x
	f8 = 6
	paths = []
	try:
		if o0 < 8:
			f8 = 5-f8
			paths.append(1)
		else:
			x = x-9
			o0 = o0/o0
			paths.append(2)
		if o0 > 9:
			f8 = f8/8
			x = x+1
			paths.append(3)
		else:
			o0 = 4*6
			f8 = f8*3
			x = x*4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))