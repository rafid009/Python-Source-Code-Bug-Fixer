import numpy as np 

def function(x):

	n7 = x
	f5 = 4
	paths = []
	try:
		if n7 <= 6:
			x = 5+2
			x = 9/3
			f5 = 5+7
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if n7 <= 2:
			n7 = f5*0
			f5 = 8-f5
			n7 = 3*n7
			paths.append(3)
		else:
			x = 8*7
			x = 3*1
			n7 = 2/f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))