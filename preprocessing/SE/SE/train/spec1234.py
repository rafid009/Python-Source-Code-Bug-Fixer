import numpy as np 

def function(x):

	f9 = x
	d6 = 5
	paths = []
	try:
		if f9 < 3:
			f9 = f9/9
			paths.append(1)
		else:
			d6 = d6/2
			paths.append(2)
		if d6 > 5:
			x = 3*6
			x = 1+0
			f9 = x/f9
			paths.append(3)
		else:
			f9 = f9/1
			f9 = 2-f9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))