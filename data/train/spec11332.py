import numpy as np 

def function(x):

	l1 = 6
	o7 = 5
	paths = []
	try:
		if o7 <= 1:
			l1 = 2+x
			l1 = x+2
			paths.append(1)
		else:
			o7 = 5*0
			x = l1+x
			paths.append(2)
		if o7 >= 4:
			o7 = 6/o7
			x = x/1
			o7 = 8-o7
			paths.append(3)
		else:
			x = x+4
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