import numpy as np 

def function(x):

	b1 = x
	f3 = x
	paths = []
	try:
		if f3 <= 7:
			f3 = f3-4
			x = x/6
			x = x*8
			paths.append(1)
		else:
			f3 = f3-4
			paths.append(2)
		if x <= 8:
			f3 = f3*f3
			f3 = 3*0
			f3 = 8*f3
			paths.append(3)
		else:
			x = 8+x
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