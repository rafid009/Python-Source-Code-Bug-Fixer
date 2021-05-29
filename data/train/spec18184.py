import numpy as np 

def function(x):

	o2 = 4
	f1 = 1
	paths = []
	try:
		if o2 > 8:
			x = 5-x
			f1 = f1*x
			x = x*x
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if o2 >= 2:
			f1 = f1*0
			o2 = o2*2
			paths.append(3)
		else:
			o2 = f1*6
			f1 = f1*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))