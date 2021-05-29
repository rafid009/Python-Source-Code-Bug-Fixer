import numpy as np 

def function(x):

	f2 = 8
	f7 = 4
	paths = []
	try:
		if f7 >= 1:
			f2 = f2/1
			f7 = 1-f7
			paths.append(1)
		else:
			x = x*f2
			x = 1*f7
			x = x/f2
			paths.append(2)
		if x < 2:
			f2 = f2/6
			f7 = f2*f7
			f7 = f7*8
			paths.append(3)
		else:
			f2 = 6+f2
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))