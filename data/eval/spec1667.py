import numpy as np 

def function(x):

	v1 = 6
	f1 = x
	paths = []
	try:
		if v1 < 9:
			f1 = 7+f1
			paths.append(1)
		else:
			x = v1/v1
			x = v1+f1
			paths.append(2)
		if f1 <= 3:
			f1 = x*0
			paths.append(3)
		else:
			f1 = f1*2
			f1 = f1/2
			f1 = f1*v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))