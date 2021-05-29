import numpy as np 

def function(x):

	f1 = x
	a7 = 6
	paths = []
	try:
		if f1 > 2:
			f1 = f1*8
			paths.append(1)
		else:
			a7 = 2-a7
			paths.append(2)
		if x < 8:
			f1 = a7-7
			a7 = a7/9
			paths.append(3)
		else:
			f1 = f1*f1
			x = a7+2
			x = x*0
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))