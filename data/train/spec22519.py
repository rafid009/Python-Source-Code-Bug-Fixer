import numpy as np 

def function(x):

	f7 = x
	r3 = x
	paths = []
	try:
		if x > 3:
			f7 = f7/r3
			x = x*9
			paths.append(1)
		else:
			r3 = r3+r3
			r3 = r3+0
			paths.append(2)
		if f7 <= 2:
			r3 = 7+4
			x = 5-2
			x = 1+x
			paths.append(3)
		else:
			r3 = f7-r3
			r3 = 1*5
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))