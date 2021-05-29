import numpy as np 

def function(x):

	f7 = x
	d2 = 8
	paths = []
	try:
		if x > 7:
			x = f7*x
			f7 = f7+f7
			f7 = x*f7
			paths.append(1)
		else:
			d2 = d2+3
			d2 = 9*8
			paths.append(2)
		if f7 >= 3:
			d2 = f7-f7
			x = 3*9
			paths.append(3)
		else:
			d2 = 6*0
			x = 7+x
			x = d2*8
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