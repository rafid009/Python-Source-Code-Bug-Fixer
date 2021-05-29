import numpy as np 

def function(x):

	f5 = 6
	a2 = x
	paths = []
	try:
		if a2 <= 2:
			x = x+0
			f5 = 0+f5
			f5 = f5-0
			paths.append(1)
		else:
			a2 = a2-7
			paths.append(2)
		if x > 8:
			f5 = f5/f5
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))