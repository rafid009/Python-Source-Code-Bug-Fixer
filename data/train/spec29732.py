import numpy as np 

def function(x):

	o2 = x
	f3 = 9
	x = x
	paths = []
	try:
		if o2 >= 4:
			o2 = o2/4
			o2 = o2-0
			x = x/x
			paths.append(1)
		else:
			f3 = f3+0
			o2 = o2-4
			paths.append(2)
		if o2 <= 3:
			o2 = 1+o2
			f3 = f3-4
			o2 = 3/x
			paths.append(3)
		else:
			o2 = o2+1
			x = x+f3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))