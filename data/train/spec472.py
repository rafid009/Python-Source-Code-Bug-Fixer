import numpy as np 

def function(x):

	f4 = x
	b7 = 9
	paths = []
	try:
		if f4 < 4:
			f4 = f4+5
			f4 = f4-1
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if b7 > 8:
			f4 = b7-f4
			f4 = f4/b7
			x = x+8
			paths.append(3)
		else:
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))