import numpy as np 

def function(x):

	f2 = x
	f6 = x
	paths = []
	try:
		if f2 > 4:
			x = f6/x
			f6 = f6+1
			paths.append(1)
		else:
			f6 = 1/x
			f6 = f6+f6
			paths.append(2)
		if f6 > 8:
			f2 = f2/f2
			paths.append(3)
		else:
			f2 = f2+8
			f2 = 8-x
			x = x*f6
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f2 = f6**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))