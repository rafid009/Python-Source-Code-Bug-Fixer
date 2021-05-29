import numpy as np 

def function(x):

	n8 = 4
	f1 = 9
	paths = []
	try:
		if x <= 2:
			f1 = 2/f1
			paths.append(1)
		else:
			x = x*3
			x = x*x
			f1 = n8-n8
			paths.append(2)
		if x < 0:
			f1 = f1-3
			x = x*2
			paths.append(3)
		else:
			n8 = n8+1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		n8 = f1**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))