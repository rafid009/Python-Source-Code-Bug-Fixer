import numpy as np 

def function(x):

	v9 = 5
	f1 = x
	paths = []
	try:
		if f1 > 7:
			x = x+v9
			f1 = f1-1
			paths.append(1)
		else:
			f1 = f1*f1
			f1 = v9-f1
			paths.append(2)
		if f1 > 7:
			f1 = f1+1
			x = 7*x
			paths.append(3)
		else:
			x = v9-x
			v9 = v9+x
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		f1 = v9**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))