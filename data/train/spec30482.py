import numpy as np 

def function(x):

	r1 = 3
	f3 = x
	x = x
	paths = []
	try:
		if f3 > 3:
			f3 = 8*f3
			x = 7+5
			f3 = 3*f3
			paths.append(1)
		else:
			r1 = x/3
			paths.append(2)
		if r1 <= 1:
			x = 1-9
			f3 = f3-6
			paths.append(3)
		else:
			f3 = 8+x
			f3 = 1-f3
			r1 = r1+x
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))