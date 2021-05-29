import numpy as np 

def function(x):

	f1 = x
	o1 = 8
	paths = []
	try:
		if o1 >= 3:
			o1 = 3/o1
			paths.append(1)
		else:
			x = f1*3
			paths.append(2)
		if x >= 8:
			o1 = o1+x
			paths.append(3)
		else:
			o1 = f1+3
			x = x/3
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))