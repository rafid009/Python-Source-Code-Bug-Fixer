import numpy as np 

def function(x):

	r8 = x
	f7 = x
	paths = []
	try:
		if f7 < 5:
			f7 = 8-4
			f7 = r8/f7
			paths.append(1)
		else:
			r8 = r8-4
			r8 = r8/r8
			f7 = f7*8
			paths.append(2)
		if f7 < 1:
			x = x+7
			f7 = f7-1
			paths.append(3)
		else:
			f7 = f7/3
			f7 = 8+r8
			f7 = f7/8
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