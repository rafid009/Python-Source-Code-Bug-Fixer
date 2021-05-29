import numpy as np 

def function(x):

	o8 = 4
	f3 = x
	x = 4
	paths = []
	try:
		if f3 >= 4:
			f3 = f3-7
			o8 = o8/o8
			x = 1+4
			paths.append(1)
		else:
			f3 = 0/f3
			x = o8*5
			f3 = f3+2
			paths.append(2)
		if o8 < 7:
			o8 = o8-x
			x = 1+x
			x = x-x
			paths.append(3)
		else:
			x = 0/x
			o8 = o8+5
			f3 = f3*o8
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))