import numpy as np 

def function(x):

	o5 = x
	f5 = x
	paths = []
	try:
		if x < 0:
			f5 = f5-4
			o5 = o5+8
			o5 = 6+o5
			paths.append(1)
		else:
			o5 = o5-5
			paths.append(2)
		if f5 <= 4:
			f5 = 6*3
			o5 = o5-o5
			paths.append(3)
		else:
			o5 = 1+0
			x = 5*o5
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f5 = x**0.5
		return f5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))