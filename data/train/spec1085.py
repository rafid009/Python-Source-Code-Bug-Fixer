import numpy as np 

def function(x):

	b3 = 4
	f8 = x
	paths = []
	try:
		if x > 8:
			b3 = 0+b3
			f8 = f8/2
			paths.append(1)
		else:
			x = 2-1
			x = x*3
			paths.append(2)
		if b3 <= 9:
			x = x-6
			b3 = b3/b3
			paths.append(3)
		else:
			b3 = 3+6
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))