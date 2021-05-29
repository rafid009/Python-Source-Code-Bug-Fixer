import numpy as np 

def function(x):

	f7 = 8
	f2 = x
	paths = []
	try:
		if f7 <= 0:
			x = 0*6
			f7 = 2+9
			paths.append(1)
		else:
			f7 = 5/f7
			paths.append(2)
		if x >= 9:
			f2 = f2*5
			x = x*0
			paths.append(3)
		else:
			f7 = 1+f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))