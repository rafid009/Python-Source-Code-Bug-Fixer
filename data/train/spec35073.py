import numpy as np 

def function(x):

	x2 = x
	f7 = 2
	paths = []
	try:
		if f7 > 5:
			x2 = x2-0
			f7 = f7/x
			x2 = x2*2
			paths.append(1)
		else:
			x = 6+x
			x = 2*x
			x = x*5
			paths.append(2)
		if x2 >= 7:
			x = f7*x
			paths.append(3)
		else:
			x = 3+x
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		f7 = x2**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))