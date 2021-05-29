import numpy as np 

def function(x):

	b4 = 4
	f2 = x
	paths = []
	try:
		if x < 8:
			f2 = f2*9
			b4 = b4-9
			f2 = 6/f2
			paths.append(1)
		else:
			f2 = 6+b4
			paths.append(2)
		if f2 <= 7:
			f2 = 4+f2
			x = 6/x
			f2 = 3-9
			paths.append(3)
		else:
			x = 4+x
			f2 = f2+7
			x = x-4
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		b4 = b4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))