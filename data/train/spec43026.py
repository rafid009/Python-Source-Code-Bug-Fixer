import numpy as np 

def function(x):

	b5 = x
	f3 = 4
	paths = []
	try:
		if f3 >= 3:
			x = x*f3
			b5 = 2/x
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if f3 > 2:
			f3 = 0+f3
			f3 = f3*f3
			paths.append(3)
		else:
			b5 = 8*2
			f3 = 1*2
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		f3 = b5**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))