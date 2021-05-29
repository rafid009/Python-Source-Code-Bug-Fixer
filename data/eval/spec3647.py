import numpy as np 

def function(x):

	b1 = 6
	f7 = 3
	paths = []
	try:
		if b1 <= 8:
			x = x*1
			f7 = 6/2
			paths.append(1)
		else:
			f7 = 5+f7
			x = x-6
			b1 = b1-4
			paths.append(2)
		if x < 1:
			x = x+x
			b1 = b1*8
			paths.append(3)
		else:
			f7 = f7/b1
			x = b1-2
			f7 = f7-7
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