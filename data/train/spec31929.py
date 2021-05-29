import numpy as np 

def function(x):

	o7 = x
	f3 = 5
	paths = []
	try:
		if o7 <= 4:
			o7 = 3+5
			x = 2-5
			f3 = f3-0
			paths.append(1)
		else:
			f3 = f3*0
			paths.append(2)
		if o7 >= 1:
			f3 = x/4
			x = 2+x
			paths.append(3)
		else:
			x = 9/f3
			f3 = 7/o7
			o7 = o7-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f3 = x**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))