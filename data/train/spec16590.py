import numpy as np 

def function(x):

	f1 = x
	n9 = 7
	paths = []
	try:
		if n9 > 6:
			f1 = 4/f1
			x = x*3
			f1 = f1/8
			paths.append(1)
		else:
			x = x*0
			paths.append(2)
		if x >= 6:
			n9 = n9-8
			paths.append(3)
		else:
			x = x/n9
			n9 = 7+7
			f1 = 1/f1
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