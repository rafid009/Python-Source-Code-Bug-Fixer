import numpy as np 

def function(x):

	f3 = 9
	b9 = x
	paths = []
	try:
		if b9 <= 3:
			f3 = f3/b9
			paths.append(1)
		else:
			f3 = 9+f3
			f3 = b9+2
			x = x-x
			paths.append(2)
		if f3 < 1:
			b9 = b9/5
			paths.append(3)
		else:
			x = 5+0
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))