import numpy as np 

def function(x):

	f1 = x
	z6 = x
	paths = []
	try:
		if f1 >= 4:
			f1 = f1*f1
			f1 = 3*z6
			paths.append(1)
		else:
			f1 = f1*2
			paths.append(2)
		if f1 > 6:
			f1 = f1/x
			f1 = 1/f1
			paths.append(3)
		else:
			x = x+1
			x = 5*f1
			z6 = 6*0
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