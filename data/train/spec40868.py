import numpy as np 

def function(x):

	f5 = 9
	a3 = x
	paths = []
	try:
		if x > 8:
			x = 2+9
			paths.append(1)
		else:
			a3 = a3+x
			x = x+f5
			x = x*2
			paths.append(2)
		if x >= 1:
			a3 = 8+5
			x = 2/f5
			paths.append(3)
		else:
			a3 = a3+a3
			f5 = f5/1
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		x = a3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))