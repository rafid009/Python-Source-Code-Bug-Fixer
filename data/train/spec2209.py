import numpy as np 

def function(x):

	o2 = x
	f6 = x
	paths = []
	try:
		if f6 > 2:
			o2 = 8/2
			f6 = 4+f6
			f6 = 3+f6
			paths.append(1)
		else:
			o2 = o2*9
			paths.append(2)
		if o2 >= 2:
			o2 = 1-o2
			o2 = 1-3
			o2 = o2/x
			paths.append(3)
		else:
			f6 = 6*o2
			x = x/6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))