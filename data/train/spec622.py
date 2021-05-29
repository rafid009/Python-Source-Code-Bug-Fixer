import numpy as np 

def function(x):

	o5 = x
	f0 = x
	paths = []
	try:
		if f0 < 8:
			f0 = 3*x
			f0 = 3*f0
			f0 = f0/1
			paths.append(1)
		else:
			o5 = o5-f0
			o5 = o5-x
			o5 = o5*1
			paths.append(2)
		if o5 <= 8:
			x = o5*4
			o5 = 4/o5
			f0 = f0+2
			paths.append(3)
		else:
			x = o5-2
			x = f0+x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		f0 = o5**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))