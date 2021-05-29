import numpy as np 

def function(x):

	f1 = x
	n8 = x
	paths = []
	try:
		if f1 > 2:
			n8 = 0*n8
			f1 = 9+1
			paths.append(1)
		else:
			x = n8+7
			paths.append(2)
		if f1 < 4:
			n8 = n8+x
			x = f1*x
			paths.append(3)
		else:
			n8 = n8+x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))