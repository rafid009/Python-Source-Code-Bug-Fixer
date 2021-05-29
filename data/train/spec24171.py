import numpy as np 

def function(x):

	b9 = 3
	f4 = x
	paths = []
	try:
		if b9 >= 2:
			b9 = 9*0
			f4 = f4+f4
			paths.append(1)
		else:
			f4 = f4/b9
			f4 = f4/3
			paths.append(2)
		if x <= 3:
			f4 = 4-6
			f4 = f4*8
			b9 = b9-b9
			paths.append(3)
		else:
			b9 = b9+4
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